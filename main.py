#tkinter chemistry calculation software
#2019.06.02 30811 남태욱

from tkinter import *
from tkinter import ttk

class App:

	def __init__(self, master):

		#농도 계산 프레임 && 프레임 화면 표시

		self.solute_mass = DoubleVar() #용질의 질량
		self.solute_molecule_weight = DoubleVar() #용질의 분자량
		#self.solvent_mass = DoubleVar() #용매의 질량
		self.solution_mass = DoubleVar() #용액의 질량
		self.solution_density = DoubleVar() #용액의 밀도

		self.solution_density.set(1.0) #용액의 밀도를 1로 설정 (변환 기능을 위해)
		self.solute_molecule_weight.set(12) #용질의 분자량을 12로 설정 (변환 기능을 위해)

		self.percent = DoubleVar() #%농도
		self.ppm = DoubleVar() #ppm농도
		self.mol = DoubleVar() #몰농도
		self.molal = DoubleVar() #몰랄농도

		frame = Frame(master)
		self.frame = frame
		frame.pack() #화면 표시

		menubar = Menu(root)

		exitmenu = Menu(menubar, tearoff=0)
		exitmenu.add_command(label='종료', command=exit)

		modmenu = Menu(menubar, tearoff=0)
		modmenu.add_command(label='농도 계산', command=self.CreateCalculationFrame)
		modmenu.add_command(label='농도 변환', command=self.CreateConversionFrame)

		menubar.add_cascade(label='프로그램', menu=exitmenu)
		menubar.add_cascade(label='모드', menu=modmenu)

		master.config(menu=menubar)

		ttk.Label(frame, text='정보 입력').grid(row=0, column=0)
		ttk.Label(frame, text='입력란').grid(row=0, column=1)
		ttk.Label(frame, text='용질의 질량(g)').grid(row=1, column=0)
		ttk.Label(frame, text='용질의 분자량').grid(row=2, column=0)
		ttk.Label(frame, text='용액의 질량(g)').grid(row=3, column=0)
		ttk.Label(frame, text='용액의 밀도(g/ml)').grid(row=4, column=0)
		ttk.Label(frame, text='버튼').grid(row=0, column=2)

		ttk.Entry(frame, textvariable=self.solute_mass).grid(row=1, column=1)
		ttk.Entry(frame, textvariable=self.solute_molecule_weight).grid(row=2, column=1)
		ttk.Entry(frame, textvariable=self.solution_mass).grid(row=3, column=1)
		ttk.Entry(frame, textvariable=self.solution_density).grid(row=4, column=1)

		ttk.Label(frame, text='결과').grid(row=5, column=0)
		ttk.Label(frame, text='출력란').grid(row=5, column=1)
		ttk.Label(frame, text='퍼센트 농도(%)').grid(row=6, column=0)
		ttk.Label(frame, text='PPM 농도(ppm)').grid(row=7, column=0)
		ttk.Label(frame, text='몰 농도(M)').grid(row=8, column=0)
		ttk.Label(frame, text='몰랄 농도(m)').grid(row=9, column=0)

		ttk.Label(frame, textvariable=self.percent).grid(row=6, column=1)
		ttk.Label(frame, textvariable=self.ppm).grid(row=7, column=1)
		ttk.Label(frame, textvariable=self.mol).grid(row=8, column=1)
		ttk.Label(frame, textvariable=self.molal).grid(row=9, column=1)

		ttk.Button(frame, text='결정', command=self.calculate).grid(row=2, column=2)
		ttk.Button(frame, text='초기화', command=self.clear).grid(row=4, column=2)

		#농도 전환 프레임

		frame2 = Frame(master)
		self.frame2 = frame2

		radioframe_from = Frame(frame2)
		self.radioframe_from = radioframe_from

		radioframe_to = Frame(frame2)
		self.radioframe_to = radioframe_to

		self.radio_selection_from = StringVar()
		self.radio_selection_to = StringVar()

		self.radio_selection_from.set('입력해주세요')
		self.radio_selection_to.set('입력해주세요')

		self.input_concentration = DoubleVar()
		self.output_concentration = DoubleVar()
		
		radio_percent_from = ttk.Radiobutton(radioframe_from, text='퍼센트 농도', variable=self.radio_selection_from, value='퍼센트 농도').grid(row=0, column=0)
		radio_mol_from = ttk.Radiobutton(radioframe_from, text='몰 농도', variable=self.radio_selection_from, value='몰 농도').grid(row=1, column=0)
		radio_molal_from = ttk.Radiobutton(radioframe_from, text='몰랄 농도', variable=self.radio_selection_from, value='몰랄 농도').grid(row=2, column=0)

		radioframe_from.grid(row=1, column=0)

		ttk.Label(frame2, text='입력값').grid(row=0, column=0)

		radio_percent_to = ttk.Radiobutton(radioframe_to, text='퍼센트 농도', variable=self.radio_selection_to, value='퍼센트 농도').grid(row=0, column=0)
		radio_mol_to = ttk.Radiobutton(radioframe_to, text='몰 농도', variable=self.radio_selection_to, value='몰 농도').grid(row=1, column=0)
		radio_molal_to = ttk.Radiobutton(radioframe_to, text='몰랄 농도', variable=self.radio_selection_to, value='몰랄 농도').grid(row=2, column=0)

		radioframe_to.grid(row=1, column=1)

		ttk.Label(frame2, text='출력값').grid(row=0, column=1)

		ttk.Label(frame2, text='^^').grid(row=0, column=2)
		ttk.Label(frame2, text='^^').grid(row=1, column=2)

		''' 테스트용도
		ttk.Label(frame2, textvariable=self.radio_selection_from).grid(row=1, column=0)
		ttk.Label(frame2, textvariable=self.radio_selection_to).grid(row=1, column=1)
		'''

		ttk.Label(frame2, text='정보 입력').grid(row=2, column=0)
		ttk.Label(frame2, text='입력란').grid(row=2, column=1)
		ttk.Label(frame2, text='버튼').grid(row=2, column=2)
		ttk.Label(frame2, textvariable=self.radio_selection_from).grid(row=3, column=0)
		ttk.Label(frame2, text='용액의 밀도(g/ml)').grid(row=4, column=0)
		ttk.Label(frame2, text='용질의 분자량').grid(row=5, column=0)

		ttk.Button(frame2, text='결정', command=self.convert).grid(row=3, column=2)
		ttk.Button(frame2, text='초기화', command=self.clear).grid(row=6, column=2)

		ttk.Entry(frame2, textvariable=self.input_concentration).grid(row=3, column=1)
		ttk.Entry(frame2, textvariable=self.solution_density).grid(row=4, column=1)
		ttk.Entry(frame2, textvariable=self.solute_molecule_weight).grid(row=5, column=1)

		ttk.Label(frame2, text='결과').grid(row=6, column=0)
		ttk.Label(frame2, text='출력란').grid(row=6, column=1)
		ttk.Label(frame2, textvariable=self.radio_selection_to).grid(row=7, column=0)
		ttk.Label(frame2, textvariable=self.output_concentration).grid(row=7, column=1)
		
	def calculate(self):

		solute_mass = self.solute_mass.get()
		solute_molecule_weight = self.solute_molecule_weight.get()
		solution_mass = self.solution_mass.get()
		solution_density = self.solution_density.get()

		percent = (solute_mass / solution_mass) * 100
		ppm = percent * 10000
		mol = ((solute_mass / solute_molecule_weight) / (solution_mass * solution_density)) * 1000
		molal = ((solute_mass / solute_molecule_weight) / (solution_mass - solute_mass)) * 1000

		self.percent.set(percent)
		self.ppm.set(ppm)
		self.mol.set(mol)
		self.molal.set(molal)

	def clear(self):

		self.solute_mass.set(0)
		self.solute_molecule_weight.set(12)
		#self.solvent_mass.set(0)
		self.solution_mass.set(0)
		self.solution_density.set(1.0)

		self.percent.set(0)
		self.ppm.set(0)
		self.mol.set(0)
		self.molal.set(0)

		self.input_concentration.set(0)
		self.output_concentration.set(0)

	def convert(self):

		#print(self.radio_selection_from.get())

		inp = self.input_concentration.get()
		density = self.solution_density.get()
		weight = self.solute_molecule_weight.get()

		
		if self.radio_selection_from.get() == '퍼센트 농도' and self.radio_selection_to.get() == '몰 농도':
			self.output_concentration.set(((inp / weight) / (100 / density)) * 1000)

		elif self.radio_selection_from.get() == '퍼센트 농도' and self.radio_selection_to.get() == '몰랄 농도':
			self.output_concentration.set(((inp / weight) / 100) * 1000)

		elif self.radio_selection_from.get() == '몰 농도' and self.radio_selection_to.get() == '퍼센트 농도':
			self.output_concentration.set(((inp * weight) / (1000 * density)) * 100)

		elif self.radio_selection_from.get() == '몰 농도' and self.radio_selection_to.get() == '몰랄 농도':
			self.output_concentration.set((inp / (1000 * density)) * 1000)

		elif self.radio_selection_from.get() == '몰랄 농도' and self.radio_selection_to.get() == '퍼센트 농도':
			self.output_concentration.set(((inp * weight) / 1000) * 100)

		elif self.radio_selection_from.get() == '몰랄 농도' and self.radio_selection_to.get() == '몰 농도':
			self.output_concentration.set((inp / (1000 / density)) * 1000)

		else: #같은거 선택 혹은 기본값
			pass

	def CreateCalculationFrame(self):

		self.frame.pack_forget()
		self.frame2.pack_forget()
		self.frame.pack()

	def CreateConversionFrame(self):

		self.frame.pack_forget()
		self.frame2.pack_forget()
		self.frame2.pack()

root = Tk()
#root.iconbitmap(default='logo.png')
root.wm_title('화학 농도 계산기 - 30811 남태욱')
#root.geometry('350x225')
#root.resizable('False', 'False')
app = App(root)
root.mainloop()
