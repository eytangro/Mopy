import Mopy.Connections.Rest.ExampleRequest

def RestExample():
    er =ExampleRequest()

    er.SetCategoryName("newCategory")
    er.SetId(12)
    er.SetPetName("Nisui")
    er.SetTagName("MyPets")

    res = er.Request()
    print (res)

RestExample()