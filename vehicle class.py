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
#تعریف کلاس موتور

class gasoline_motor(motor):
    def __init__(self,motor_id:str,Cylinder_volume:float,number_of_Cylinder:int,spark_plug_material:str):
        super().__init__(motor_id, Cylinder_volume, number_of_Cylinder)
        self.spark_plug_material=spark_plug_material
    def description(self):
        print(f"a gasoline motor with the {self.motor_volume} liters volume and {self.number_of_Cylinder} Cylinders with the {self.spark_plug_material} spark plugs and registered by id : {self.motor_id}")
    def start(self):
        print('gasoline motor turned on')
#تعریف کلاس موتور بنزینی با راث بری از موتور و چیادی سازی متد های استارت و دیسکریپشن (پیاده سازی abstraction)
class disel_motor(motor):
    def __init__(self, motor_id, Cylinder_volume, number_of_Cylinder):
        super().__init__(motor_id, Cylinder_volume, number_of_Cylinder)
    def description(self):
       print(f"a disel motor with the {self.motor_volume} liters volume and {self.number_of_Cylinder} Cylinders and registered by id : {self.motor_id}") 
    def start(self):
        print('disel motor turned on')
#پیاده سازی کلاس موتور دیزلی همانند موتور بنزینی

gasoline_motor_1=gasoline_motor('S212341', 1.5, 4, 'Cu')
gasoline_motor_1.description()
disel_motor_1=disel_motor('D465558', 1.5, 4)
disel_motor_1.description()
#تست کلاس ها
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
        return f"this device made by {self.company} with the serial number : {self.serial_number}"
    def set_volume(self,new_volume):
        if self.status:
            self.volume=new_volume
            print(f"volume : {self.volume}")
        else :
            print("system is off")
        
    def set_music(self,new_song):
        if self.status:
            self.music=new_song
            print(f"music {self.music} started")
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

#پیاده سازی کلاس سیستم صوتی و تست آن (این کلاس برای مفهوم aggregation طراحی شده است)
###################################################################

class vehicle:
    def __init__(self,company:str,owner:str,Plaque_number:str,motor_id : str):
        self.company=company
        self._owner=owner
        self.Plaque_number=Plaque_number
        self._motor_id=motor_id
        self.status=False
    def lock(self):
        print('vehicle locked')
    def unlock(self):
        print('vehicle unloked')
    def move(self):
        raise ValueError("please define move method")
    def description(self):
        raise ValueError("please define description method")
    def turn_on(self):
        raise ValueError("please define turn_on method")
    def turn_off(self):
        raise ValueError("please define turn_off method")        
    
V=vehicle('company', 'Erfan', '65b617', 's88dq44')
#V.description()

#ساخت کلاس وسیله نقلیه
################################################################
class car(vehicle):
    def __init__(self, company, owner, Plaque_number, motor_id,number_of_passengers : int,color : str):
        super().__init__(company, owner, Plaque_number, motor_id)
        self.number_of_passengers=number_of_passengers
        self.color=color
    def move(self):
        raise ValueError("please define move method")
    def description(self):
        raise ValueError("please define description method")        
    def turn_on(self):
        if not self.status:
            print('the car turned on')
            self.status=True
        else:
            print('the car is already turned on')
    def turn_off(self) :
        if self.status :
            print('the car turned off')
            self.status=False
        else:
            print('the car is already turned off')
    def lock(self):
        print('the car is locked')
    def unlock(self):
        print("the car unlocked")

#ساخت کلاس ماشین سواری با ارث بری از کلاس وسیله ی نقلیه و تعریف متد های لاک و انلاک به شکل متفاوت از کلاس والد (پیاده سازی مفهوم polymorphism)
car1=car('benz','Arman keshazar','8585F6969','B88845',4,'black')
car1.turn_on()
###############################################################
class pride(car):
    def __init__(self, company, owner, Plaque_number, motor_id, number_of_passengers, color, model : str , sound_system:sound_system, chassis_number : str):
        super().__init__(company, owner, Plaque_number, motor_id, number_of_passengers, color)
        self.motor=gasoline_motor(motor_id, 0.330, 4, 'Pt')
        self.sound_system=sound_system
        self._chassis_number=chassis_number
        self.number_of_passengers=number_of_passengers
    def move(self):
        print("pride is moving")
    def description(self):
        print(f"a {self.color} pride with model {self.model} and Plaque{self.Plaque_number}")
        print(f"Technical Specifications : made by {self.company}, can ride with maximum {self.number_of_passengers} passengers,chassis number:{self._chassis_number} and have :")
        self.motor.description()
        print(f'owner : {self._owner}')
    def sound_condition(self):
        if self.sound_system==None:
            print('this pride doesnt have sound device')
        else:
            if self.sound_system.status:
                if self.sound_system.music != None:
                    print(f'music {self.sound_system.music} is playing with volume : {self.sound_system.volume}')
                else:
                    print('device is on but no music is playing')
            else:
                print("sound system is turned off")
    def turn_on(self):
        if not self.status:
            self.motor.start()
            print('pride turned on')
            self.status=True
        else:
            print('pride is already turned on')
    def turn_off(self):
        if self.status:
            self.motor.turn_off()
            print('pride turned off')
            self.status=False
        else:
            print("pride is already turned off")
#پیاده سازی کلاس پراید با ارث بری از کلاس ماشین سواری و تعریف ویژگی ها و متد ها
################################################
    
class xian(car):
    def __init__(self, company, owner, Plaque_number, motor_id, number_of_passengers, color, model : str , chassis_number : str):
        super().__init__(company, owner, Plaque_number, motor_id, number_of_passengers, color)
        self.model=model
        self.motor=gasoline_motor(motor_id, 1.5, 4, 'Pt')
        self._chassis_number=chassis_number
        self.number_of_passengers=number_of_passengers
    def move(self):
        print("xian is moving")
    def description(self):
        print(f"a {self.color} xian with model {self.model} and Plaque{self.Plaque_number}")
        print(f"Technical Specifications : made by {self.company}, can ride with maximum {self.number_of_passengers} passengers,chassis number:{self._chassis_number} and have :",end=' ')
        self.motor.description()
        print(f'owner : {self._owner}')

    def turn_on(self):
        if not self.status:
            self.motor.start()
            print('xian turned on')
            self.status=True
        else:
            print('xian is already turned on')
    def turn_off(self):
        if self.status:
            self.motor.turn_off()
            print('xian turned off')
            self.status=False
        else:
            print("xian is already turned off")

x1=xian("company", "owner", "Plaque_number", "motor_id", 4, "color", "model", "chassis_number")
x1.description()
#تعریف کلاس ژیان و تست آن 
#############################################
class Peugeot_206(car):
    def __init__(self, company, owner, Plaque_number, motor_id, number_of_passengers, color, model : str , sound_system:sound_system, chassis_number : str):
        super().__init__(company, owner, Plaque_number, motor_id, number_of_passengers, color)
        self.motor=gasoline_motor(motor_id, 1.5, 4, 'Pt')
        self.sound_system=sound_system
        self._chassis_number=chassis_number
        self.number_of_passengers=number_of_passengers
        self.model=model
    def move(self):
        print("Peugeot 206 is moving")
    def description(self):
        print(f"a {self.color} Peugeot 206 with model {self.model} and Plaque{self.Plaque_number}")
        print(f"Technical Specifications : made by {self.company}, can ride with maximum {self.number_of_passengers} passengers,chassis number:{self._chassis_number} and have :",end=' ')
        self.motor.description()
        print(f'owner : {self._owner}')
    def sound_condition(self):
        if self.sound_system==None:
            print('this Peugeot 206 doesnt have sound device')
        else:
            if self.sound_system.status:
                if self.sound_system.music != None:
                    print(f'music {self.sound_system.music} is playing with volume : {self.sound_system.volume}')
                else:
                    print('device is on but no music is playing')
            else:
                print("sound system is turned off")
    def turn_on(self):
        if not self.status:
            self.motor.start()
            print('Peugeot 206 turned on')
            self.status=True
        else:
                print('Peugeot 206 is already turned on')
    def turn_off(self):
        if self.status:
            self.motor.turn_off()
            print('Peugeot 206 turned off')
            self.status=False
        else:
            print("Peugeot 206 is already turned off")            
sound_system_soltan206=sound_system('opco', 'OD2000js')
soltan206=Peugeot_206('iran khodro', 'Mohammad Shabestari', '73j344', 'Ps93012', 5, 'black', 87, sound_system_soltan206, 'NAAPC319381kApE39')
sound_system_soltan206.turn_on()
sound_system_soltan206.set_music('Nazanin by Dariush')
sound_system_soltan206.set_volume(20)
soltan206.description()
#تعریف کلاس پژو 206 و تست آن و تست سیستم صوتی
#############################
class Toyota_hilux(car):
    def __init__(self, company, owner, Plaque_number, motor_id, number_of_passengers, color, model : str , sound_system:sound_system, chassis_number : str):
        super().__init__(company, owner, Plaque_number, motor_id, number_of_passengers, color)
        self.motor=disel_motor(motor_id, 0.7, 4)
        self.sound_system=sound_system
        self._chassis_number=chassis_number
        self.model=model
    def move(self):
        print("Toyota hilux is moving")
    def description(self):
        print(f"a {self.color} Toyota hilux with model {self.model} and Plaque{self.Plaque_number}")
        print(f"Technical Specifications : made by {self.company}, can ride with maximum {self.number_of_passengers} passengers,chassis number:{self._chassis_number} and have :",end=' ')
        self.motor.description()
        print(f'owner : {self._owner}')
    def sound_condition(self,sound_system):
        if self.sound_system==None:
            print('this Toyota hilux doesnt have sound device')
        else:
            if self.sound_system.status:
                if self.sound_system.music != None:
                    print(f'music {self.sound_system.music} is playing with volume : {self.sound_system.volume}')
                else:
                    print('device is on but no music is playing')
            else:
                print("sound system is turned off")
    def turn_on(self):
        if not self.status:
            self.motor.start()
            print('Toyota hilux turned on')
            self.status=True
        else:
                print('Toyota hilux is already turned on')
    def turn_off(self):
        if self.status:
            self.motor.turn_off()
            print('Toyota hilux turned off')
            self.status=False
        else:
            print("Toyota hilux is already turned off")
#تعریف کلاس تویوتا هیلوکس                
######################################
class elantra(car):
    def __init__(self, company, owner, Plaque_number, motor_id, number_of_passengers, color, model : str , sound_system:sound_system, chassis_number : str, have_gps:bool):
        super().__init__(company, owner, Plaque_number, motor_id, number_of_passengers, color)
        self.motor=gasoline_motor(motor_id, 0.4, 4, 'Cu')
        self.sound_system=sound_system
        self._chassis_number=chassis_number
        self.have_gps=have_gps
        self.model=model
    def move(self):
        print("elantra is moving")
    def description(self):
        print(f"a {self.color} elentra with model {self.model} and Plaque{self.Plaque_number}")
        print(f"Technical Specifications : made by {self.company}, can ride with maximum {self.number_of_passengers} passengers,chassis number:{self._chassis_number} and have :",end=' ')
        self.motor.description()
        print(f'owner : {self._owner}')
    def sound_condition(self):
        if self.sound_system==None:
            print('this elantra doesnt have sound device')
        else:
            if self.sound_system.status:
                if self.sound_system.music != None:
                     print(f'music {self.sound_system.music} is playing with volume : {self.sound_system.volume}')
                else:
                    print('device is on but no music is playing')
            else:
                print("sound system is turned off")
    def turn_on(self):
            if not self.status:
                self.motor.start()
                print('elantra turned on')
                self.status=True
            else:
                print('elantra is already turned on')
    def turn_off(self):
            if self.status:
                self.motor.turn_off()
                print('elantra turned off')
                self.status=False
            else:
                print("elantra is already turned off")
    def show_location(self):
        if self.have_gps:
            print('show location of the car')
        else:
            print('this elantra does not have gps')

#تعریف کلاس النترا
#########################################
class motorcycle(vehicle):
    def __init__(self, company, owner, Plaque_number, motor_id, color : str , have_painting : bool):
        super().__init__(company, owner, Plaque_number, motor_id)
        self.color=color
        self.have_painting=have_painting
    def move(self):
        raise ValueError("please define move method")
    def description(self):
        raise ValueError("please define description method")        
    def turn_on(self):
        if not self.status:
            print('the motorcycle turned on')
            self.status=True
        else:
            print('the motorcycle is already turned on')
    def turn_off(self) :
        if self.status :
            print('the motorcycle turned off')
            self.status=False
        else:
            print('the motorcycle is already turned off')
    def lock(self):
        print('the motorcycle is locked')
    def unlock(self):
        print("the motorcycle unlocked")

#تعریف کلاس موتورسیکلت
##########
class Honda_Activa(motorcycle):
    def __init__(self, company, owner, Plaque_number, motor_id, color, have_painting,model,chassis_number):
        super().__init__(company, owner, Plaque_number, motor_id, color, have_painting)
        self.model=model
        self._chassis_number=chassis_number
        self.motor=motor(motor_id, 0.124, 1)
    def move(self):
        print("Honda Activa is moving")
    def turn_on(self):
        if not self.status:
            self.motor.start()
            print('Honda Activa turned on')
            self.status=True
        else:
            print('Honda Activa is already turned on')
    def turn_off(self):
            if self.status():
                self.motor.turn_off()
                print('elantra turned off')
                self.status=False
            else:
                print("elantra is already turned off")    
    def description(self):
        if self.have_painting:
            print(f"a {self.color} Honda Activa and have painting and its model is {self.model} and Plaque{self.Plaque_number}")
        else:
            print(f"a {self.color} Honda Activa and its model is {self.model} and Plaque{self.Plaque_number}")
        
        print(f"Technical Specifications : made by {self.company}, chassis number:{self._chassis_number} and have ",end='')
        self.motor.description()
        print('owner : {self._owner}')

#تعریف کلاس موتور سیکلت هوندا اکتیوا
####################
class Yamaha_WR450(motorcycle):
    def __init__(self, company, owner, Plaque_number, motor_id, color, have_painting,model,chassis_number):
        super().__init__(company, owner, Plaque_number, motor_id, color, have_painting)
        self.model=model
        self._chassis_number=chassis_number
        self.motor=motor(motor_id, 0.450, 1)
    def move(self):
        print("Yamaha WR450 is moving")
    def turn_on(self,motor):
        if not self.status:
            self.motor.start()
            print('Yamaha WR450 turned on')
            self.status=True
        else:
            print('Yamaha WR450 is already turned on')
    def turn_off(self,motor):
            if self.status():
                self.motor.turn_off()
                print('Yamaha WR450 turned off')
                self.status=False
            else:
                print("Yamaha WR450 is already turned off")    
    def description(self):
        if self.have_painting:
            print(f"a {self.color} Yamaha WR450 and have painting and its model is {self.model} and Plaque{self.Plaque_number}")
        else:
            print(f"a {self.color} Yamaha WR450 and its model is {self.model} and Plaque{self.Plaque_number}")
        
        print(f"Technical Specifications : made by {self.company}, chassis number:{self._chassis_number} and have ",end='')
        self.motor.description()
        print(f'owner : {self._owner}')
#تعریف کلاس موتور سیکلت یاماها WR450
########################

class heavy_vehicle(vehicle):
    def __init__(self, company, owner, Plaque_number, motor_id,color,number_of_wheels,extera_lights : bool):
        super().__init__(company, owner, Plaque_number, motor_id)
        self.color=color
        self.number_of_wheels=number_of_wheels
        self.extra_lights=extera_lights
    def move(self):
        raise ValueError("please define move method")
    def description(self):
        raise ValueError("please define description method")        
    def turn_on(self):
        if not self.status:
            print('the heavy vehicle turned on')
            self.status=True
        else:
            print('heavy vehicle is already turned on')
    def turn_off(self) :
        if self.status :
            print('heavy vehicle turned off')
            self.status=False
        else:
            print('heavy vehicle is already turned off')
    def lock(self):
        print('heavy vehicle is locked')
    def unlock(self):
        print("heavy vehicle unlocked")

#تعریف کلاس ماشین سنگین
#############

class dump_truck(heavy_vehicle):
    def __init__(self, company, owner, Plaque_number, motor_id, color, number_of_wheels,number_of_Cylinder,Cylinder_volume, extera_lights,model,chassis_number,bare_weight):
        super().__init__(company, owner, Plaque_number, motor_id, color, number_of_wheels, extera_lights)
        self.model=model
        self._chassis_number=chassis_number
        self.bare_weight=bare_weight
        self.motor=disel_motor(motor_id, Cylinder_volume, number_of_Cylinder)
    def move(self):
        print("dump truck is moving")
    def description(self):
        print(f"a {self.color} dump truck with model {self.model} and Plaque{self.Plaque_number} ")
        print(f"Technical Specifications : made by {self.company},  maxium load : {self.bare_weight} tons,chassis number:{self._chassis_number} and have :" , end='')
        self.motor.description()
        print('owner : {self._owner}')

    def turn_on(self):
        if not self.status:
            self.motor.start()
            print('dump truck turned on')
            self.status=True
        else:
            print('dump truck is already turned on')
    def turn_off(self):
        if self.status:
            self.motor.turn_off()
            print('dump truck turned off')
            self.status=False
        else:
            print("dump truck is already turned off")
            
d1=dump_truck('company', 'owner', 'Plaque_number', 'motor_id', 'color', 18, 6, 2.5, 'extera_lights', 'model', 'chassis_number', 10)
d1.turn_on()

#تعریف کلاس دامپ تراک و تست آن
##########

class trailer(heavy_vehicle):
    def __init__(self, company, owner, Plaque_number, motor_id, color, number_of_wheels,Cylinder_volume,number_of_Cylinder , extera_lights,model,chassis_number,bare_weight):
        super().__init__(company, owner, Plaque_number, motor_id, color, number_of_wheels, extera_lights)
        self.model=model
        self._chassis_number=chassis_number
        self.bare_weight=bare_weight
        self.motor=disel_motor(motor_id, Cylinder_volume, number_of_Cylinder)
    def move(self):
        print("trailer is moving")
    def description(self):
        print(f"a {self.color} trailer with model {self.model} and Plaque{self.Plaque_number} ")
        print(f"Technical Specifications : made by {self.company},  maxium load : {self.bare_weight} tons,chassis number:{self._chassis_number} and have :" , end='')
        self.motor.description()
        print('owner : {self._owner}')

    def turn_on(self):
        if not self.status:
            self.motor.start()
            print('trailer turned on')
            self.status=True
        else:
            print('trailer is already turned on')
    def turn_off(self):
        if self.status:
            self.motor.turn_off()
            print('trailer turned off')
            self.status=False
        else:
            print("trailer is already turned off")    

t1=trailer('company', 'owner', 'Plaque_number', 'motor_id', 'color', 10, 2.5, 6, True, 'model', 'chassis_number', 10)
t1.turn_on()
#تعریف کلاس تریلر و تست آن
###############################    
class bus(heavy_vehicle):
    def __init__(self, company, owner, Plaque_number, motor_id, color, number_of_wheels,Cylinder_volume,number_of_Cylinder , extera_lights,model,chassis_number,number_of_passengers):
        super().__init__(company, owner, Plaque_number, motor_id, color, number_of_wheels, extera_lights)
        self.model=model
        self._chassis_number=chassis_number
        self.number_of_passengers = number_of_passengers
        self.motor=disel_motor(motor_id, Cylinder_volume, number_of_Cylinder)
    def move(self):
        print("bus is moving")
    def description(self):
        print(f"a {self.color} bus with model {self.model} and Plaque{self.Plaque_number} ")
        print(f"Technical Specifications : made by {self.company},  maxium load : {self.number_of_passengers},chassis number:{self._chassis_number} and have :",sep='')
        self.motor.description()
        print(f'owner : {self._owner}')

    def turn_on(self):
        if not self.status:
            self.motor.start()
            print('bus turned on')
            self.status=True
        else:
            print('bus is already turned on')
    def turn_off(self):
        if self.status :
            self.motor.turn_off()
            print('bus turned off')
            self.status=False
        else:
            print("bus is already turned off")       
 
    
    
bus1=bus('company', 'owner', 'Plaque_number', 'motor_id', 'color', 10, 5, 4, True, "model", "chassis_number", 40)
bus1.description()

#تعریف کلاس اتوبوس و تست آن


