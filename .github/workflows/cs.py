from http import HTTPStatus
import dashscope

dashscope.api_key = "sk-5f813c697a3d4d9bbcbb5fafce82fd55"
def tongyi(que):
    response = dashscope.Generation.call(
        model=dashscope.Generation.Models.qwen_turbo,
        prompt=que
   )
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if response.status_code == HTTPStatus.OK:
#		print(response.output)
        return response.output["text"]  # The output text
#        print(response.usage)  # The usage information
    else:
        return response.code  # The error code.
#        print(response.message)  # The error message.

if __name__ == '__main__':
    print(tongyi("Hello"))
