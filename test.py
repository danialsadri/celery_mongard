from main import add, add_bind, division_bind
from celery import chain, group, chord, chunks

# -----------------------------------------------------------------------
# Signatures
# result = division_bind.signature((5, 5)).delay()
# print(result)

# Partials
# result = division_bind.signature((5,)).delay(5)
# print(result)

# Callbacks
# result = division_bind.apply_async((5, 5), link=add.signature((5,)))
# print(result)

# Immutability
# result = division_bind.apply_async((5, 5), link=add.signature((5, 5), immutable=True))
# print(result)
# -----------------------------------------------------------------------
# result = chain(add.s(5, 5), add_bind.s(5))
# print(result().get())
# -----------------------------------------------------------------------
# result = group(add.s(5, 5), add_bind.s(5, 5))
# print(result().get())
# -----------------------------------------------------------------------
# result = chord(add.s(5, 5), add_bind.s(5, 5))(division_bind.s(5, 5))
# print(result.get())
# -----------------------------------------------------------------------
# result = add.chunks(zip(range(10), range(100)), 10)
# print(result())
# -----------------------------------------------------------------------
