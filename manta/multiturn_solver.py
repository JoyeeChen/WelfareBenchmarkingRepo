"""
MANTA Multi-Turn Solver
Custom Inspect AI solver that handles multi-turn adversarial conversations
"""

# The conversation engine. This is a custom Inspect AI solver that:

# Reads the turns from the scenario metadata
# Executes the conversation step-by-step:
# Send Turn 1 → Get model response
# Send Turn 2 → Get model response
# Send Turn 3 → Get model response (if 3/4-turn)
# Send Turn 4 → Get model response (if 4-turn)
# Returns the complete conversation in the state object
# Without this custom solver, Inspect AI would only do single-turn Q&A. This solver makes the multi-turn adversarial pressure work.

from inspect_ai.solver import Solver, solver, Generate
from inspect_ai.model import ChatMessageUser, ChatMessageAssistant, get_model


@solver
def multi_turn_conversation():
    """
    Custom solver that conducts multi-turn conversations using turns from metadata.

    For each sample:
    1. Model responds to Turn 1 (base question)
    2. Add Turn 2 (pressure) and get model response
    3. Continue for all turns in the scenario
    4. Final state contains the complete conversation
    """

    async def solve(state, generate):
        # Get the turns from metadata
        all_turns = state.metadata.get('all_turns', [])

        if not all_turns:
            # Fallback to simple generation if no turns in metadata
            return await generate(state)

        # Start with the first turn already in state.messages
        # (It was added from Sample.input)

        # Generate response to Turn 1
        state = await generate(state)

        # Now add subsequent turns
        for turn in all_turns[1:]:  # Skip first turn, already processed
            # Add the adversarial follow-up as a user message
            state.messages.append(
                ChatMessageUser(content=turn['content'])
            )

            # Generate model's response
            state = await generate(state)

        # Return final state with complete conversation
        return state

    return solve


# Alternative: Simpler version that just generates all turns at once
@solver
def simple_multiturn():
    """
    Simpler multi-turn solver - adds all user turns upfront,
    then generates all responses in sequence.
    """

    async def solve(state, generate):
        all_turns = state.metadata.get('all_turns', [])

        if len(all_turns) <= 1:
            return await generate(state)

        # Clear existing messages and rebuild from all_turns
        state.messages = []

        for i, turn in enumerate(all_turns):
            # Add user message
            state.messages.append(
                ChatMessageUser(content=turn['content'])
            )

            # Generate assistant response
            state = await generate(state)

        return state

    return solve
