class Pro:
	def __init__(self, id):
		self.id = id
		self.act = True

class GFG:
	def __init__(self):
		self.TotalProcess = 0
		self.process = []
	
	def initialiseGFG(self):
		print("Número de processos --> ")
		self.TotalProcess = 5
		self.process = [Pro(i) for i in range(self.TotalProcess)]
	
	def Election(self):
		print("Processo de numero " + str(self.process[self.FetchMaximum()].id) + " falhou")
		self.process[self.FetchMaximum()].act = False
		print("Eleicao iniciada com 2 processos")
		initializedProcess = 2

		old = initializedProcess
		newer = old + 1

		while (True):
			if (self.process[newer].act):
				print("Processo " + str(self.process[old].id) + " fez eleição(" + str(self.process[old].id) + ") para " + str(self.process[newer].id))
				old = newer
			newer = (newer + 1) % self.TotalProcess
			if (newer == initializedProcess):
				break

		print("Processo " + str(self.process[self.FetchMaximum()].id) + " se torna o coordenador")
		coord = self.process[self.FetchMaximum()].id

		old = coord
		newer = (old + 1) % self.TotalProcess
		while (True):
			if (self.process[newer].act):
				print("Processo " + str(self.process[old].id) + " passa coordenador(" + str(coord) + ") mensagem para processar " + str(self.process[newer].id))
				old = newer
			newer = (newer + 1) % self.TotalProcess
			if (newer == coord):
				print("fim da eleicao ")
				break
	
	def FetchMaximum(self):
		maxId = -9999
		ind = 0
		for i in range(self.TotalProcess):
			if (self.process[i].act and self.process[i].id > maxId):
				maxId = self.process[i].id
				ind = i
		return ind

def main():
	object = GFG()
	object.initialiseGFG()
	object.Election()

if __name__ == "__main__":
	main()
