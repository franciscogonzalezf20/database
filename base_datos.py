from datetime import datetime
from tortoise import Tortoise, fields
from tortoise import Model

class Sat(Model):
    candado = fields.CharField(max_length=25,index=True)
    id_contenedor = fields.CharField(max_length=4,index=True)
    numero_integracion = fields.CharField(max_length=25, primary_key=True, index=True)
    numero_gafete_unico = fields.CharField(null=True, max_length=25)
    operacion_interna = fields.CharField(max_length=12,index=True)
    estatus_notificado = fields.CharField(max_length=50,index=True)
    

class Estatus(Model):
    id_estatus = fields.IntField(primary_key=True, index=True)
    descripcion_estatus = fields.CharField(max_length=35,index=True)
    fecha_inicial = fields.DatetimeField(index=True)
    fecha_liberacion = fields.DatetimeField(index=True)
    numero_integracion = fields.ForeignKeyField("models.Sat", related_name="estatus", index=True,max_length=25)
    

class Pedimento(Model):
    id_pedimento = fields.IntField(primary_key=True, index=True)
    tipo_pedimento = fields.CharField(max_length=30,index=True)
    numero_pedimento = fields.CharField(max_length=25,index=True)
    remesa = fields.CharField(max_length=8,null=True)
    numero_acuse = fields.CharField(max_length=15,null=True)
    tipo_operacion = fields.CharField(max_length=13,index=True)
    clave = fields.CharField(max_length=3,index=True)
    identificacion_vehiculo = fields.CharField(max_length=15,index=True)
    cantidad_mercancias = fields.CharField(max_length=3,null=True)
    numero_integracion = fields.ForeignKeyField("models.Sat", related_name="pedimentos", index=True,max_length=25)

class PagoPedimento(Model):
    id_pago = fields.IntField(primary_key=True, index=True)
    linea_captura = fields.CharField(index=True,max_length=22)
    banco = fields.CharField(index=True,max_length=50)
    fecha_pago = fields.DatetimeField(index=True)
    numero_operacion_bancaria = fields.CharField(index=True,max_length=15)
    numero_transaccion_sat = fields.CharField(index=True,max_length=20)
    clave_prevalidador = fields.CharField(index=True,max_length=2)
    id_pedimento = fields.ForeignKeyField("models.Pedimento", related_name="pagospedimento", index=True)


class Bitacora(Model):
    id_bitacora = fields.IntField(pk=True, index=True)
    numero_integracion = fields.CharField(max_length=25, index=True)
    consultado = fields.BooleanField(index=True)
    estatus_final = fields.BooleanField(index=True)
    descripcion = fields.CharField(max_length=255, index=True)
    fecha_consulta = fields.DatetimeField(auto_now=True, index=True)


class Meta:
    table = "bitacora"
