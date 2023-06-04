from .models import User_info,Contact_info
from .serializers import User_infoSerializer
from .serializers import Contact_infoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,exceptions
import json

# Create your views here.
class Login_List(APIView):    
    def post(self, request):
        username=request.data.get('user_name',None)
        password = request.data.get('password', None)
        # print(username)
        if not username:
            return Response({"Provide Username"}, status=404)
        if not password:
            return Response({"Provide password"}, status=404)

        try:
            obj_data=User_info.objects.get(user_name=username,password=password)
            if obj_data:    
                return Response({"Logged In"},
                    status=200,
                        )
            else:
                return Response(
                    json.dumps({"False Information is Provided"}),
                    status=400
                    )
        except :
            return Response(
                    json.dumps({"False Information is Provided"}),
                    status=400
                    )

class Signup_List(APIView):    
    def post(self, request):
        user_name=request.data.get('username',None)
        password = request.data.get('password', None)
        email_address = request.data.get('email_address', None)
        phone_number = request.data.get('phone_number', None)
        if phone_number is None:
            return Response(
                json.dumps({'Error': "Phone No. is Missing"}),
                status=404,
                content_type="application/json"
                )
        try:
            obj_data=User_info.objects.get(phone_number=phone_number)
        except :
            obj_data = None
        if obj_data:
            return Response(
                json.dumps({'Error': "Phone No. already Exist"}),
                status=409,
                content_type="application/json"
            )
        else:
            user = User_info(
                user_name=user_name,
                password=password,
                email_address=email_address,
                phone_number=phone_number
                )
            try:
                user.save()
                return Response(
                    json.dumps({'user_name': user.user_name}),
                    status=200, 
                    content_type="application/json"
                )
            except : 
                # print(e)
                return Response(
                    json.dumps({'Error': "Error in signup"}),
                    status=400,
                    content_type="application/json"
                )
  

class Contact_Info_List(APIView):
    def get(self, request,user_id=None):
        # print (user_id)
        contacts = Contact_info.objects.filter(user_id=user_id)
        serializer = Contact_infoSerializer(contacts, many=True)
        return Response(serializer.data)
    

    def post(self, request, user_id=None):
            contact_arr = request.data.get('data', None)
            try:
                user_info_obj=User_info.objects.get(id=user_id)
            except Exception as e:
                return Response(
                    json.dumps({'Error': "User does not exist. Please provide valid user."}),
                    status=404,
                    content_type="application/json"
                ) 
                
            if contact_arr is None:
                return Response(
                    json.dumps({'Error': "No Contacts provided to add."}),
                    status=404,
                    content_type="application/json"
                )
                               
            # print(user_info_obj)
            for  contact in contact_arr:
                contact_obj = Contact_info(
                    user_id=user_info_obj,
                    contact_name=contact["user_name"],
                    contact_phone_number=contact["phone_number"]
                )
                
                try:
                    contact_obj.save()
                except Exception as e:
                    return Response(
                        json.dumps({'Error': "Error saving contact with phone number %s "% contact_obj['contact_phone_number']}),
                        status=400,
                        content_type="application/json"
                    )
                    
            return Response(json.dumps({'Success': "contacts got saved successfully !!!"}),
                status=200,
                content_type="application/json")

    def put(self, request, user_id=None):
        
        contact_phone_number =request.data.get("contact_phone_number", None)
        contact_name = request.data.get("contact_user_name", None)
        is_spam = request.data.get("is_spam", None)
        
        if not contact_phone_number:
            return Response(
                    json.dumps({'Error': "Phone no. is missing"}),
                    status=400,
                    content_type="application/json"
                )
    
        contact_obj = Contact_info.objects.filter(contact_phone_number = contact_phone_number,user_id=user_id).first()
        if contact_name:
            contact_obj.contact_name=contact_name
        if is_spam is not None:
            contact_obj.is_spam = is_spam
            
        try:
            contact_obj.save()
        except Exception as e:
                    return Response(
                        json.dumps({'Error': "Error updating contact with phone number %s "% contact_obj['contact_phone_number']}),
                        status=400,
                        content_type="application/json"
                    )
        
        return Response(
                json.dumps({"Error":'Contact Updated Successfully'}),
                status=200,
                content_type="application/json"
            )

class Search_Name(APIView):
    def get(self,request):
        user_name=request.query_params.get('user_name')
        if  not user_name:
            return Response(
                    json.dumps({'Error': "Username is mandatory"}),
                    status=400,
                    content_type="application/json")
        else:
            Contact_list=Contact_info.objects.filter(contact_name=user_name)
            serializer = Contact_infoSerializer(Contact_list, many=True)
           
            return Response(serializer.data)
        

class Search_Phone(APIView):
    def get(self,request):
        phone_number=request.query_params.get('phone_number')
        
        if not phone_number:
            return Response(
                    json.dumps({'Error': "Phone no. is mandatory"}),
                    status=400,
                    content_type="application/json"
                )
        else:
            Contact_list=Contact_info.objects.filter(contact_phone_number=phone_number)
            if len(Contact_list) > 0:
                for contact in Contact_list:
                    try:
                        registered_contact_obj = User_info.objects.filter(phone_number = phone_number)
                        user_list = User_infoSerializer(registered_contact_obj, many=True)
                        user_obj = user_list.data[0]
                        
                        setattr(contact, "contact_name", user_obj["user_name"])
                        setattr(contact, "email", user_obj["email_address"])
                    except Exception as e:
                        print("return none", e)
                        registered_contact_obj = None
                    
                
            serializer = Contact_infoSerializer(Contact_list, many=True)
           
            return Response(serializer.data)
        