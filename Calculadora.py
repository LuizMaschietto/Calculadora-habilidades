import abc
from tkinter import*
from tkinter import font

class Application:
    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.sexContainer = Frame(master)
        self.sexContainer["padx"] = 20
        self.sexContainer.pack()

        self.hepContainer = Frame(master)
        self.hepContainer["padx"] = 20
        self.hepContainer.pack()

        self.octContainer = Frame(master)
        self.octContainer["padx"] = 20
        self.octContainer.pack()
                
        self.nineContainer = Frame(master)
        self.nineContainer["padx"] = 20
        self.nineContainer.pack()
        

        

        self.titulo = Label(self.primeiroContainer, text="Calculadora Atributos")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        # Segundo
        #self.nivelLabel = Label(self.segundoContainer,text="Nivel", font=self.fontePadrao)
        #self.nivelLabel.pack(side=LEFT)

        #self.nivel = Entry(self.segundoContainer)
        #self.nivel["width"] = 5
        #self.nivel["font"] = self.fontePadrao
        #self.nivel.pack(side=LEFT)
        # Terceiro
        self.aptiLabel = Label(self.terceiroContainer, text="Aptidão", font=self.fontePadrao)
        self.aptiLabel.pack(side=LEFT)

        self.apti = Entry(self.terceiroContainer)
        self.apti["width"] = 5
        self.apti["font"] = self.fontePadrao
        self.apti.pack(side=LEFT)
        # Quarto
        self.agiLabel = Label(self.quartoContainer, text="agilidade",font=self.fontePadrao)
        self.agiLabel.pack(side=LEFT)

        self.Agilidade = Entry(self.quartoContainer)
        self.Agilidade["font"] = self.fontePadrao
        self.Agilidade["width"] = 5
        self.Agilidade.pack(side=LEFT)

        #Quinto
        self.conheLabel = Label(self.quintoContainer, text="conhecimento", font=self.fontePadrao)
        self.conheLabel.pack(side=LEFT)

        self.conhe = Entry(self.quintoContainer)
        self.conhe["width"] = 5
        self.conhe["font"] = self.fontePadrao
        self.conhe.pack(side=LEFT)
        #Sexto
        self.forLabel = Label(self.sexContainer, text="Força Fisica", font=self.fontePadrao)
        self.forLabel.pack(side=LEFT)

        self.força = Entry(self.sexContainer)
        self.força["width"] = 5
        self.força["font"] = self.fontePadrao
        self.força.pack(side=LEFT)
        #Setimo
        self.sorLabel = Label(self.hepContainer, text="Sorte", font=self.fontePadrao)
        self.sorLabel.pack(side=LEFT)

        self.sor = Entry(self.hepContainer)
        self.sor["width"] = 5
        self.sor["font"] = self.fontePadrao
        self.sor.pack(side=LEFT)
        #oct
        self.vitLabel = Label(self.octContainer, text="Vitalidade", font=self.fontePadrao)
        self.vitLabel.pack(side=LEFT)

        self.vit = Entry(self.octContainer)
        self.vit["width"] = 5
        self.vit["font"] = self.fontePadrao
        self.vit.pack(side=LEFT)
        #Botao
        self.calcular = Button(self.nineContainer)
        self.calcular["text"] = "calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.abreJanela
        self.calcular.pack()
    
    def abreJanela(self):
        novaJanela= Toplevel(root)
        atributos=CalculaAtributos()
        atributos.calculaAtrib(self)
        T= Text(root,height=5,width=52)
        effectAgilidade = "Velocidade de movimento: "+str(atributos.move) +"\nDano Dex: " +str(atributos.danoDex) +"\nEsquiva: "+str(atributos.esquiva)+"\nAtaques Extras: "+str(atributos.numeroAtaques)
        effectAptidao= "Mana maxima: "+str(atributos.manaMAX)+"\nDano Magias: "+str(atributos.danoMagia)+"\nTempo Reduzido de Cast: "+str(atributos.castReduzido)+"\nEfetividade de Cast: "+str(atributos.potenciaCast)+"\nPode Ter magias preparadas: "+str(atributos.preparaCast)
        effectForca= "Peso Que Aguenta(KGs): "+str(atributos.forçaMAX)+"\nDano STR: "+str(atributos.danoSTR)+"\nResistencia a Blunt: "+str(atributos.resistenciaBLUNT)+"\nChance De Atordoar(em %): "+str(atributos.stagChance)
        effectVitalidade= "Dados Extras de Vida:"+str(atributos.vidaExtra)+"\nResistencia a Efeitos(%):"+str(atributos.chanceResist)+"\nRegen de Vida PASSIVO:"+str(atributos.regenPassivo)+"\nRegen De Vida COMBATE: "+str(atributos.regenCombate)
        effectConhecimento= "Regen De Mana PASSIVO: "+str(atributos.regenManaPassiva)+"\nRegen de Mana COMBATE: "+str(atributos.regenManaCombate)+"\nEfetividade de Magias de Suporte: "+ str(atributos.supEffect)+"\nTempo para regenerar mana(turno): "+str(atributos.regenTurno)
        effectSorte="Acerto:"+str(atributos.acerto)+"\nDano de Critico: "+str(atributos.danoCRIT)+"\nQuantidade De Lucky Points: "+str(atributos.luckPoints)+"\nEfeito da Sorte: "+str(atributos.sorteEffect)
        effectImunidades="Imunidades:\n"+"Stun: "+str(atributos.imunidadeSTUN)+"\nBIND: "+str(atributos.imunidadeBIND)+"\nVenenos Simples: "+str(atributos.imunidadeVida)
        novaJanela.title("Efeitos")
        # novaJanela.geometry ("300x500")
        Label(novaJanela,text="Efeitos Dos Atributos.").pack()
        Label(novaJanela,text= "------------------AGILIDADE------------------").pack()
        Label(novaJanela,text=effectAgilidade).pack()
        Label(novaJanela,text= "------------------SORTE------------------").pack()
        Label(novaJanela,text=effectSorte).pack()
        Label(novaJanela,text= "------------------FORÇA------------------").pack()
        Label(novaJanela,text=effectForca).pack()
        Label(novaJanela,text= "---------------VITALIDADE------------------").pack()
        Label(novaJanela,text=effectVitalidade).pack()
        Label(novaJanela,text= "----------------CONHECIMENTO-----------------").pack()
        Label(novaJanela,text=effectConhecimento).pack()
        Label(novaJanela,text= "------------------APTIDÃO------------------").pack()
        Label(novaJanela,text=effectAptidao).pack()
        Label(novaJanela,text= "------------------IMUNIDADES------------------").pack()
        Label(novaJanela,text=effectImunidades).pack()





class CalculaAtributos:

    #Calcula Atributo
    def calculaAtrib(self,info: Application) -> None:

       # self.nivel = int(info.nivel.get())
        agilidade= int(info.Agilidade.get())
        aptidao=int(info.apti.get())
        força=int(info.força.get())
        vitalidade=int(info.vit.get())
        conhecimento=int(info.conhe.get())
        sorte=int(info.sor.get())
        #agilidade stats
        self.move=agilidade/5
        self.danoDex=agilidade/25
        self.esquiva=((agilidade/50) +(sorte/25)) 
        self.numeroAtaques=agilidade/100
        if agilidade>=1000:
            self.imunidadeBIND=True
        else:
            self.imunidadeBIND=False

        #aptidao Stats
        self.manaMAX=(aptidao +(conhecimento/25))
        self.danoMagia=aptidao/25
        self.castReduzido=aptidao/50
        self.potenciaCast=aptidao/100
        if aptidao>=1000:
            self.preparaCast=True
        else:
            self.preparaCast=False
        

        #Força Stats
        self.forçaMAX=força/5
        self.danoSTR=força/25
        self.resistenciaBLUNT=força/50
        self.stagChance=força/100
        if força >=1000:
            self.imunidadeSTUN=True
        else:
            self.imunidadeSTUN=False


        #vitalidade Stats
        self.vidaExtra=vitalidade/5
        self.chanceResist=vitalidade/25
        self.regenPassivo=vitalidade/50
        self.regenCombate=vitalidade/100
        if vitalidade>=1000:
            self.imunidadeVida=True
        else:
            self.imunidadeVida=False

        #conhecimento Stats
        self.regenManaPassiva=conhecimento
        self.regenManaCombate=conhecimento/5
        self.supEffect = conhecimento/100
        if conhecimento>=1000:
            self.regenTurno = 1
        else:
            self.regenTurno = 5
        
        #sorte Stats
        self.acerto= sorte/5
        self.danoCRIT= sorte/100
        self.luckPoints= sorte/500
        if sorte>=1000:
            self.sorteEffect=True
        else:
            self.sorteEffect=False
            
    

root = Tk()
Application(root)
root.mainloop()