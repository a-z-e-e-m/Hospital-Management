class staff:
  def __init__(self,name,phone,email,):
    self.name=name
    self.phone=phone
    self.email=email
  def purchase_parking_pass(self):   
    print("purchase pass is provided to "+self.name+" with phone number "+str(self.phone)+str(self.email))
class Medical_staff(staff):
  def __init__(self,department,block):
    self.department=department
    self.block=block
  def attent_a_patient(self):
    print("patient proceeded to the "+self.department+" department "+" block "+self.block)
class Non_Medical_staff(staff):
  def __init__(self,types,duty_area):
    self.types=types
    self.duty_area=duty_area
  def fill_logbook(self):
    print("go and fill the logbook")
class doctor(Medical_staff):
  def __init__(self,room_no,on_call_day,specialization):
    self.room_no=room_no
    self.on_call_day=on_call_day
    self.specialization=specialization
  def medicine(self):
    print("Prescribe the medicine to room number "+str(self.room_no))
  def test(self):
    print("prescribe the test to the patient at specialization "+self.specialization)
class nurse(Medical_staff):
  def __init__(self,floor,off_day):
    self.floor=floor
    self.off_day=off_day
  def vital(self):
    print("take vital info of the patient at the floor "+str(self.floor))
  def patient(self):
    print("organize patient details from the floor "+str(self.floor))           



S1=staff("Famitha",9876543210,"famitha@gamil.com")
S1.purchase_parking_pass()
S2=Medical_staff("orthology","A")
S2.attent_a_patient()
S3=Non_Medical_staff("security","gate")
S3.fill_logbook()
S4=doctor(5,"thursday","orthology")
S4.medicine()
S4.test()
S5=nurse(4,"Sunday")
S5.vital()
S5.patient()
