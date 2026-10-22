# import pytest
# from string_processor import StringProcessor
#
# @pytest.mark.parametrize(
#     "input_text, expected_output",
#     [
#         ("hello", "Hello."),
#         ("Hello", "Hello."),
#         ("hello world", "Hello world."),
#     ],
# )
# def test_process_positive(input_text, expected_output):
#     processor = StringProcessor()
#     assert processor.process(input_text) == expected_output
#
# @pytest.mark.parametrize(
#     "input_text, expected_output",
#     [("", "."), ("    ", "    .")],
# )
# def test_process_negative(input_text, expected_output):
#     processor = StringProcessor()
#     assert processor.process(input_text) == expected_output

# import pytest
# from string_processor import StringProcessor
#
# @pytest.mark.parametrize('old_str, new_str', [ ('hello', 'Hello.'), ('Hello', 'Hello.'), ('hello world', 'Hello world.') ] )
# def test_new_string_positive(old_str, new_str):
#     res = StringProcessor.process(old_str)
#     assert res == new_str
#
# @pytest.mark.parametrize('old_str, new_str', [('', '.'), (' ', ' .'), ('!', '!.'), ('8', '8.')])
# def test_new_string_negative(old_str, new_str):
#     res = StringProcessor.process(old_str)
#     assert res == new_str