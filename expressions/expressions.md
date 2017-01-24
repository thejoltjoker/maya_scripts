# Useful Maya Expressions

## Play every other frame of alembic
if (frame % 2 == 0)
	node_AlembicNode.time = frame + 1;