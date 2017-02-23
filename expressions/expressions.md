# Useful Maya Expressions

## Play every other frame of alembic
```
*remove the + 1 to do even frames*
if (frame % 2 == 0)
	example_AlembicNode.time = time + 1;
```