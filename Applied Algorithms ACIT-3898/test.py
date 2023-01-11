import unittest

from solution import our_shared_values


class TrulySharedValues(unittest.TestCase):
    def test_two_empty(self):
        self.assertCountEqual(our_shared_values([], []), [])

    def test_empty_on_left(self):
        self.assertCountEqual(our_shared_values([], ["lima", "foxtrot"]), [])

    def test_empty_on_right(self):
        self.assertCountEqual(our_shared_values(["lima", "foxtrot"], []), [])

    def test_both_identical_one_word(self):
        self.assertCountEqual(our_shared_values(["oscar"], ["oscar"]), ["oscar"])

    def test_both_identical_two_word(self):
        self.assertCountEqual(
            our_shared_values(["cats", "dogs"], ["cats", "dogs"]), ["cats", "dogs"]
        )

    def test_three_words_shuffled(self):
        self.assertCountEqual(
            our_shared_values(
                ["cats", "dogs", "squirrels"], ["squirrels", "dogs", "cats"]
            ),
            ["cats", "dogs", "squirrels"],
        )

    def test_more_on_the_left(self):
        self.assertCountEqual(
            our_shared_values(["cats", "dogs", "squirrels"], ["squirrels", "dogs"]),
            ["dogs", "squirrels"],
        )

    def test_more_on_the_right(self):
        self.assertCountEqual(
            our_shared_values(["cats", "dogs", "squirrels"], ["squirrels", "dogs"]),
            ["dogs", "squirrels"],
        )

    def test_more_on_both(self):
        self.assertCountEqual(
            our_shared_values(["grape", "fruit"], ["fruit", "bat"]), ["fruit"]
        )

    def test_double_dogs_both(self):
        self.assertCountEqual(
            our_shared_values(
                ["cats", "dogs", "squirrels", "dogs"],
                ["squirrels", "dogs", "dogs", "cats"],
            ),
            ["dogs", "cats", "dogs", "squirrels"],
        )

    def test_triple_dogs_both(self):
        self.assertCountEqual(
            our_shared_values(
                ["cats", "dogs", "dogs", "squirrels", "dogs"],
                ["squirrels", "dogs", "dogs", "cats", "dogs"],
            ),
            ["dogs", "cats", "dogs", "squirrels", "dogs"],
        )

    def test_double_dogs_left(self):
        self.assertCountEqual(
            our_shared_values(
                ["cats", "dogs", "squirrels", "dogs"], ["squirrels", "cats"]
            ),
            ["cats", "squirrels"],
        )

    def test_double_dogs_left_more(self):
        self.assertCountEqual(
            our_shared_values(
                ["cats", "dogs", "squirrels", "dogs"], ["squirrels", "dogs", "cats"]
            ),
            ["dogs", "cats", "squirrels"],
        )

    def test_triple_dogs_right(self):
        self.assertCountEqual(
            our_shared_values(
                ["cats", "dogs", "squirrels", "dogs"],
                ["squirrels", "dogs", "dogs", "cats", "dogs"],
            ),
            ["dogs", "cats", "dogs", "squirrels"],
        )

    def test_triple_dogs_right_more(self):
        self.assertCountEqual(
            our_shared_values(
                ["cats", "dogs", "squirrels"],
                ["squirrels", "dogs", "dogs", "cats", "dogs"],
            ),
            ["cats", "dogs", "squirrels"],
        )


    def test_triple_cats(self):
        self.assertCountEqual(
            our_shared_values(
                ["cats", "cats", "cats", "dogs", "squirrels"],
                ["squirrels", "cats", "cats", "dogs", "dogs", "cats", "dogs"],
            ),
            ["cats", "dogs", "cats", "cats", "squirrels"],
        )
    
    def test_shorter_with_doubles(self):
        self.assertCountEqual(
            our_shared_values(
                ["dogs","dogs"],
                ["cats","dogs","squirrels","squirrels"]
            ),
            ["dogs"]
        )