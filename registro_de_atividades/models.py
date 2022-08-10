from django.db import models

# Create your models here.
class Topico(models.Model):
	'''Um tópico ou assunto sobre o qual será registrado'''
	texto = models.CharField(max_length=200)
	data_criacao = models.DateField(auto_now_add=True)

	def __str__(self):
		'''Devolve uma representação em string do modelo'''
		return self.texto

class Entry(models.Model):
	"""Algo especifico aprendido sobre o assunto"""
	topico  = models.ForeignKey(Topico, on_delete=models.CASCADE)
	texto = models.TextField()
	data_criacao = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Devolve uma representação em string do modelo."""
		#return self.texto[:50] + '...' if len(self.texto) > 50:  
		if len(self.texto) > 50:
			return self.texto[:50] + '...'
		return self.texto


