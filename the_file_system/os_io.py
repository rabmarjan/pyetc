import io
from functools import wraps

output = io.StringIO()
output.write("This goes int othe buffer")
print("And so does this.", file=output)
print(output.getvalue())
output.close()

input = io.StringIO("Initial value for read buffer")
print(input.read())

output = io.BytesIO()
output.write('This goes into the buffer. '.encode('utf-8'))
output.write('ÁÇÊ'.encode('utf-8'))

print(output.getvalue())
output.close()
input = io.BytesIO(b'Inital value for read buffer')
print(input.read())

output = io.BytesIO()
wrapper = io.TextIOWrapper(
    output,
    encoding='utf-8',
    write_through=True,
)
wrapper.write('This goes into the buffer. ')
wrapper.write('ÁÇÊ')

print(output.getvalue())
output.close()
input = io.BytesIO(
    b'Inital value for read buffer with unicode characters ' +
    'ÁÇÊ'.encode('utf-8')
)
wrapper = io.TextIOWrapper(input, encoding='utf-8')
print(wrapper.read())


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper


@debug
def add(a, b):
    return a + b


print(add(3, 4))
