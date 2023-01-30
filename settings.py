from tortoise import Tortoise

async def init():
  
  await Tortoise.init(
  db_url='postgresql://fran:password@host:5432/cursos',
  modules={'models': ['base_datos']}
 )
  await Tortoise.generate_schemas()
