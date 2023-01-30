from datetime import datetime
from tortoise import Tortoise, fields
from tortoise import Model

class Sat(Model):
    candado = fields.CharField(index=True)
    id_caja = fields.CharField(index=True)
    numero_integracion = fields.CharField(max_length=255, primary_key=True, index=True)
    numero_gafete_unico = fields.CharField(null=True, max_length=255)
    estado = fields.CharField(index=True)
    fecha_administrativa = fields.DatetimeField(default=datetime.utcnow, index=True)
    operacion_interna = fields.CharField(index=True)
    estatus_notificado = fields.CharField(index=True)
    

class Estatus(Model):
    id_estatus = fields.IntField(primary_key=True, index=True)
    descripcion_estatus = fields.CharField(index=True)
    fecha_inicial = fields.DatetimeField(index=True)
    fecha_liberacion = fields.DatetimeField(index=True)
    numero_integracion = fields.ForeignKeyField("models.Sat", related_name="estatus", index=True)
    

class Pedimento(Model):
    id_pedimento = fields.IntField(primary_key=True, index=True)
    tipo = fields.CharField(index=True)
    numero_pedimento = fields.CharField(index=True)
    remesa = fields.CharField(null=True)
    numero_acuse = fields.CharField(null=True)
    tipo_operacion = fields.CharField(index=True)
    clave = fields.CharField(index=True)
    identificacion_vehiculo = fields.CharField(index=True)
    cantidad_mercancias = fields.CharField(null=True)
    numero_integracion = fields.ForeignKeyField("models.Sat", related_name="pedimentos", index=True)

class PagoPedimento(Model):
    id_pago = fields.IntField(primary_key=True, index=True)
    linea_captura = fields.CharField(index=True)
    banco = fields.CharField(index=True)
    fecha_pago = fields.DatetimeField(index=True)
    numero_operacion_bancaria = fields.CharField(index=True)
    numero_transaccion_sat = fields.CharField(index=True)
    clave_prevalidador = fields.CharField(index=True)
    id_pedimento = fields.ForeignKeyField("models.Pedimento", related_name="pagospedimento", index=True)


class Bitacora(Model):
    id_bitacora = fields.IntField(pk=True, index=True)
    numero_integracion = fields.CharField(max_length=100, index=True)
    consultado = fields.CharField(max_length=100, index=True)
    estatus_final = fields.CharField(max_length=100, index=True)
    descripcion = fields.CharField(max_length=100, index=True)
    fecha_consulta = fields.DatetimeField(auto_now=True, index=True)

class Meta:
    table = "bitacora"