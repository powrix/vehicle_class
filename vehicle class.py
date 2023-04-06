class motor:
    def __init__(self,motor_id:str,Cylinder_volume:float,number_of_Cylinder:int):
        self.motor_id=motor_id
        self.Cylinder_volume=Cylinder_volume
        self.number_of_Cylinder=number_of_Cylinder
        self.motor_volume=Cylinder_volume*number_of_Cylinder
    def start(self):
        raise ValueError("please define start method")
    def turn_off(self):
        print('the motor has turned off')
    def description(self):
        raise ValueError("please define description method")

class gasoline_motor(motor):
    def __init__(self,motor_id:str,Cylinder_volume:float,number_of_Cylinder:int,spark_plug_material:str):
        super().__init__(motor_id, Cylinder_volume, number_of_Cylinder)
        self.spark_plug_material=spark_plug_material
    def description(self):
        print(f"a gasoline motor with the {self.motor_volume} liters volume and {self.number_of_Cylinder} Cylinders with the {self.spark_plug_material} spark plugs and registered by id : {self.motor_id}")
    def start(self):
        print('gasoline motor turned on')

class disel_motor(motor):
    def __init__(self, motor_id, Cylinder_volume, number_of_Cylinder):
        super().__init__(motor_id, Cylinder_volume, number_of_Cylinder)
    def description(self):
       print(f"a disel motor with the {self.motor_volume} liters volume and {self.number_of_Cylinder} Cylinders and registered by id : {self.motor_id}") 



gasoline_motor_1=gasoline_motor('S212341', 1.5, 4, 'Cu')
gasoline_motor_1.description()
disel_motor_1=disel_motor('D465558', 1.5, 4)
disel_motor_1.description()

#################################################################

class sound_system:
    def __init__(self, company : str, serial_number : str):
        self.company=company
        self.serial_number=serial_number
        self.volume=0
        self.music=None
        self.status=False
    def description(self):
        print(f"this device made by {self.company} with the serial number : {self.serial_number}")
    def set_volume(self,new_volume):
        if self.status:
            self.volume=new_volume
            print(f"volume : {self.volume}")
        else :
            print("system is off")
        
    def set_music(self,new_song):
        if self.status:
            self.music=new_song
            print("music {self.music} started")
        else:
            print("system is off")
    def turn_on(self):
        print('system turned on')
        self.status=True
    def turn_off(self):
        print('system turned off')
        self.status = False
    
device_1=sound_system('HARMAN', 'Sdf19039j2')
device_1.description()
device_1.turn_on()
device_1.set_music('Dastaye to by Dariush')
###################################################################

        

