import pytest
from watch import parse


def test_1():
    assert (
        parse("http://youtube.com/embed/xvFZjo5PgG0") == "http://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse("https://youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse("https://www.youtube.com/embed/xvFZjo5PgG0")
        == "https://youtu.be/xvFZjo5PgG0"
    )

    assert (
        parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "http://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse(
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in -picture" allowfullscreen></iframe>'
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse(
            '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
        )
        == None
    )
