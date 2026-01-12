import pytest
from um import count


def test_1():
    assert (
        count(
            "I think, um, we should probably head out now if we want to beat the traffic."
        )
    ) == 1
    assert (
        count(
            "The presentation went well, but I, um, um, I think I forgot to mention the final budget figures."
        )
    ) == 2
    assert (
        count(
            "Wait, let me see if I can find my keys; they were just, um, um, um, right here on the counter a second ago."
        )
    ) == 3
    assert (
        count(
            "Um, I'm not entirely sure how to answer that question without checking the files first."
        )
    ) == 1
    assert (
        count(
            "If we decide to go with the blue paint, then, um, we'll need to buy extra rollers and, um, maybe some drop cloths too."
        )
    ) == 2
    assert (count("And have a lovely day, yourself")) == 0
    assert (count("My tummy is fully of yummy icecream")) == 0
