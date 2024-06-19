# En usuarios/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre=None, apellido=None, password=None):
        if not correo:
            raise ValueError('El correo electrónico es obligatorio')
        user = self.model(
            correo=self.normalize_email(correo),
            nombre=nombre,
            apellido=apellido
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password, nombre=None, apellido=None):
        user = self.create_user(
            correo=correo,
            nombre=nombre,
            apellido=apellido,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=80, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

class Oauth(models.Model):
    expiryDate = models.DateTimeField()
    token = models.CharField(max_length=255)
    tokenRefresh = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Token de {self.usuario.nombre}"

class Tarea(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fechaVencimiento = models.DateTimeField()
    estado = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

class HistorialTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=200)

    def __str__(self):
        return f"Detalle de {self.tarea.titulo}"
