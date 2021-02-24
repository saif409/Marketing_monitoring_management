from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Country, District, Division, SubDistrict, ServiceCategory, Package
from django.contrib import messages
from django.core.paginator import Paginator
from.models import SubDistrict,Surveyor,Division,District,CollectData,AssignDataCollector
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

# Create your views here.


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('admin_home')
    else:
        if request.method == "POST":
            user = request.POST.get('user', )
            password = request.POST.get('pass', )
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('admin_home')
            else:
                messages.add_message(request, messages.ERROR, 'Username or password mismatch!')
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect('login')


def admin_home(request):
    if request.user.is_authenticated:
        assign_collector_obj = AssignDataCollector.objects.all()[::-1]
        total_data_collector = Surveyor.objects.all().count()
        total_data_collect = CollectData.objects.all().count()
        total_assign_data_collector = AssignDataCollector.objects.all().count()

        context={
            "isact_home":"active",
            "total_data_collector":total_data_collector,
            "total_data_collect":total_data_collect,
            "total_assign_data_collector":total_assign_data_collector,
            "data": assign_collector_obj
        }
        return render(request, "admin_home.html", context)
    else:
        return redirect('login')


def create_collect_form(request):
    if request.user.is_authenticated:
        user_obj = Surveyor.objects.all()[::-1]
        country_obj = Country.objects.all()
        division_obj = Division.objects.all()
        district_obj = District.objects.all()
        subdistrict_obj = SubDistrict.objects.all()
        context={
            "isact_assigndatacollector":"active",
            "user":user_obj,
            "country":country_obj,
            "division":division_obj,
            "district":district_obj,
            "subdistrict":subdistrict_obj

        }
        if request.method == "POST":
            company_name = request.POST.get("company_name")
            service_category = request.POST.get("service_category")
            u_obj = request.POST.get("assign_data_collector")
            assign_data_collector=User.objects.get(username=u_obj)
            assign_by = request.user
            area = request.POST.get("area")
            country_obj = request.POST.get("country")
            country = Country.objects.get(country_name=country_obj)
            division_obj = request.POST.get("division")
            division = Division.objects.get(division_name=division_obj)
            district_obj = request.POST.get("district")
            district = District.objects.get(district_name=district_obj)
            sub_district_obj = request.POST.get("sub_district")
            sub_district = SubDistrict.objects.get(sub_district_name=sub_district_obj)
            collect_obj = AssignDataCollector(company_name=company_name, service_category=service_category,assign_data_collector=assign_data_collector,
                                              assign_by=assign_by, area=area, country=country, division=division,district=district,sub_district=sub_district)
            collect_obj.save()
            messages.success(request, "Data Collector Assign Successfully")
            return redirect(admin_home)
        return render(request, "assign_data_collector/assign_data_collect_form.html", context)
    else:
        return ('login')


def view_form(request, id):
    if request.user.is_authenticated:

        obj =get_object_or_404(AssignDataCollector, id=id)
        context={
            "obj":obj
        }
        return render(request, "assign_data_collector/view_form.html", context)
    return redirect('login')


def form_delete(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(AssignDataCollector, id=id)
        obj.delete()
        messages.success(request, "Data Deleted Successfully")
        return redirect('admin_home')
    else:
        return redirect('login')


def surveyor_list(request, filter):
    if request.user.is_authenticated:
        user_obj = None
        if filter == 'None':
            user_obj = Surveyor.objects.all()[::-1]
        elif filter == 'active':
            user_obj = Surveyor.objects.all().filter(status=1)[::-1]
        elif filter == 'inactive':
            user_obj = Surveyor.objects.all().filter(status=2)[::-1]
        elif filter == 'rejected':
            user_obj = Surveyor.objects.all().filter(status=3)[::-1]

        context ={
            "isact_surveyorlist": "active",
            "user": user_obj
        }
        return render(request, "surveyor/surveyor_list.html", context)
    else:
        return redirect('login')


def view_surveyor(request, id):
    if request.user.is_authenticated:
        user_obj = Surveyor.objects.get(id=id)
        user_obj_another = user_obj.user
        data_obj = CollectData.objects.all().filter(data_collector=user_obj_another)
        total_collect_data = CollectData.objects.all().filter(data_collector=user_obj_another).count()
        context= {
            "user": user_obj,
            "data":data_obj,
            "total_collect_data":total_collect_data,
            "isact_surveyorlist": "active",
        }
        return render(request, "surveyor/view_surveyor.html", context)
    else:
        return redirect('login')


def update_surveyor(request, id):
    if request.user.is_authenticated:
        user_obj = get_object_or_404(Surveyor, id=id)
        if request.method == "POST":
            user_obj.address = request.POST.get("address")
            user_obj.profile_picture = request.POST.get("profile_picture")
            user_obj.country = request.POST.get("country")
            user_obj.division = request.POST.get("division")
            user_obj.district = request.POST.get("district")
            user_obj.sub_district = request.POST.get("sub_district")
            user_obj.email = request.POST.get("email")
            user_obj.graduation_subject = request.POST.get("graduation_subject")
            user_obj.university = request.POST.get("university")
            user_obj.Skills = request.POST.get("Skills")
            user_obj.area = request.POST.get("area")
            user_obj.phone = request.POST.get("phone")
            user_obj.description = request.POST.get("description")
            user_obj.designation = request.POST.get("designation")
            user_obj.experience = request.POST.get("experience")
            user_obj.role = request.POST.get("role")
            user_obj.status = request.POST.get("status")
            user_obj.save()
            messages.success(request, "User Update Successfully !!")
            return redirect('update_surveyor', id=id)

        context ={
            "user": user_obj,
            "isact_surveyorlist": "active",
        }
        return render(request, "surveyor/surveyor_update.html", context)
    else:
        return redirect('login')


def remove_surveyor(request, id):
    obj = get_object_or_404(User, id=id)
    obj.delete()
    messages.success(request, "Requested User Delete Successfully !!")
    return redirect('surveyor_list', 'None')


def register_surveyor(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fname = request.POST.get('fname', )
            lname = request.POST.get('lname', )
            uname = request.POST.get('uname', )
            password = request.POST.get('password', )
            address = request.POST.get("address")
            profile_picture = request.FILES.get("profile_picture")
            country = request.POST.get("country")
            division = request.POST.get("division")
            district = request.POST.get("district")
            sub_district = request.POST.get("sub_district")
            email = request.POST.get("email")
            area = request.POST.get("area")
            phone = request.POST.get("phone")
            designation = request.POST.get("designation")
            experience = request.POST.get("experience")
            description = request.POST.get("description")
            graduation_subject = request.POST.get("graduation_subject")
            university = request.POST.get("university")
            user = User.objects.all().filter(username=uname)
            if user :
                messages.success(request, "User Already Exits")
                return redirect('register_surveyor')
            else :
                auth_info={
                    'first_name': fname,
                    'last_name': lname,
                    'username': uname,
                    'password': make_password(password),
                }
                user = User(**auth_info)
                user.save()
            user_obj = Surveyor(experience=experience,university=university,description=description,graduation_subject=graduation_subject,user=user,address=address,profile_picture=profile_picture,country=country,division=division,
                                district=district,sub_district=sub_district,email=email,area=area,
                                phone=phone,designation=designation)
            user_obj.save()
            messages.success(request, "Data Collector Create Successfully !!")
        context = {
            "isact_registersurveyor": "active"
        }
        return render(request, "surveyor/register_surveyor.html", context)
    else:
        return redirect('login')


def country(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            country_name = request.POST.get("country")
            user = Country(country_name=country_name)
            user.save()
            messages.success(request, "Country Added Successfully")

        get_country = Country.objects.all()[::-1]
        context = {
            "get_country": get_country,
            'isact_location': 'active',
        }
        return render(request, "add/add_country.html", context)
    else:
        return redirect('login')


def country_remove(request, id):
    obj = get_object_or_404(Country, id=id)
    obj.delete()
    messages.success(request, "Country Remove Successfully")
    return redirect('country')


def add_division(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            division_name = request.POST.get("division")
            user = Division(division_name=division_name)
            user.save()
            messages.success(request, "Division Added Successfully")
        div_obj = Division.objects.all()[::-1]
        paginator = Paginator(div_obj, 10)
        page = request.GET.get('page')
        get_page = paginator.get_page(page)
        context = {
            "div_obj": get_page,
            'isact_location': 'active',
        }
        return render(request, "add/add_division.html", context)
    else:
        return redirect('login')


def add_district(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            district_name = request.POST.get("district")
            user = District(district_name=district_name)
            user.save()
            messages.success(request, "District Added Successfully")

        get_district = District.objects.all()[::-1]
        paginator = Paginator(get_district, 10)
        page = request.GET.get('page')
        get_page = paginator.get_page(page)
        context = {
            "get_district": get_page,
            'isact_location': 'active',
        }
        return render(request, "add/add_district.html", context)
    else:
        return redirect('login')


def update_district(request, id):
    if request.user.is_authenticated:

        obj = get_object_or_404(District, id=id)
        context={
            "district":obj,
            'isact_location': 'active'
        }
        if request.method == "POST":
            obj.district_name = request.POST.get("district")
            obj.save()
            messages.success(request, "District Update Successfully")
            return redirect(add_district)
        return render(request, "update/update_district.html", context)
    else:
        return redirect('login')


def remove_district(reuquest, id):
    obj = get_object_or_404(District, id=id)
    obj.delete()
    messages.success(reuquest, "District Removed Successfully ")
    return redirect(add_district)

def add_sub_district(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            sub_district_name = request.POST.get("sub_district")
            user = SubDistrict(sub_district_name=sub_district_name)
            user.save()
            messages.success(request, "Sub District Added Successfully")
        get_subdistrct = SubDistrict.objects.all()[::-1]
        paginator = Paginator(get_subdistrct, 10)
        page = request.GET.get('page')
        get_page = paginator.get_page(page)
        context = {
            "get_subdistrct": get_page,
            'isact_location': 'active',
        }
        return render(request, "add/add_subdistrict.html", context)
    else:
        return redirect('login')


def update_sub_district(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(SubDistrict, id=id)
        context={
            "obj":obj,
            'isact_location': 'active'
        }
        if request.method == "POST":
            obj.sub_district_name = request.POST.get("sub_district")
            obj.save()
            messages.success(request, "Sub District Update Successfully")
            return redirect(add_sub_district)
        return render(request, "update/sub_district_update.html", context)
    else:
        return redirect('login')


def remove_subdistrict(request, id):
    obj = get_object_or_404(SubDistrict, id=id)
    obj.delete()
    messages.success(request, "Sub District Remove Successfully")
    return redirect(add_sub_district)



def notifications(request):
    if request.user.is_authenticated:
        user_obj = Surveyor.objects.all()[::-1]
        context = {
            "user": user_obj,
            'isact_notification': 'active',
        }
        if request.method == "POST":
            send_to = request.POST.get('oxdoraitech@gmail.com')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            recipient = request.POST.get('recipient')
            check_obj = Surveyor.objects.filter(email=recipient)

            if check_obj.exists():
                send_mail("Mail Subject : "+subject, message,send_to, [recipient], fail_silently=False)
                if send_mail:
                    messages.success(request, "Your Email Successfully Send !!!")
                else:
                    messages.success(request, "Send Fail ")
            else:
                messages.success(request, "Mail Does not Exists")
        return render(request, "notification/create_notification.html", context)
    else:
        return redirect('login')


def collecting_data_list(request):
    if request.user.is_authenticated:
        data = CollectData.objects.all()[::-1]

        context={
            "data": data,
            "isact_datacollectlist":"active"
        }
        return render(request, "data_collect/data_collection_list.html", context)
    else:
        return redirect('login')


def create_data_form(request):
    if request.user.is_authenticated:
        context={
            "isact_createsurvey":"active"
        }
        if request.method == "POST":
            visited_company_name = request.POST.get("visited_company_name")
            contact_person_name = request.POST.get("contact_person_name")
            designation_of_contact_person = request.POST.get("designation_of_contact_person")
            service_category = request.POST.get("service_category")
            contact_no = request.POST.get("contact_no")
            email = request.POST.get("email")
            address = request.POST.get("address")
            picture_visited_person = request.FILES.get("picture")
            package_name = request.POST.get("package_name")
            description = request.POST.get("description")
            collector_obj = CollectData(data_collector=request.user, visited_company_name=visited_company_name, contact_person_name=contact_person_name,
                                        designation_of_contact_person=designation_of_contact_person, service_category=service_category, contact_no=contact_no,
                                        email=email, address=address, picture_visited_person=picture_visited_person, package_name=package_name, description=description)

            collector_obj.save()
            messages.success(request, "Collect Data Store Successfully")
            return redirect(create_data_form)
        return render(request, "data_collect/create_data_form.html", context)
    else:
        return redirect('login')


def collect_data_view(request, id):
    if request.user.is_authenticated:
        data = get_object_or_404(CollectData, id=id)
        context ={
            "data":data,
            "isact_datacollectlist": "active"
        }
        return render(request, "data_collect/collect_data_view.html", context)
    else:
        return redirect('login')


def collect_data_delete(request, id):
    obj = get_object_or_404(CollectData, id=id)
    obj.delete()
    messages.success(request, "Data Deleted Successfully !!")
    return redirect("collecting_data_list")


def update_country(request, id):
    if request.user.is_authenticated:
        country_obj = get_object_or_404(Country, id=id)
        context = {
            "country":country_obj,
            'isact_location': 'active'
        }
        if request.method == "POST":
            country_obj.country_name = request.POST.get("country")
            country_obj.save()
            messages.success(request, "Country Name Update Successfully")
            return redirect(country)

        return render(request, "update/update_country.html", context)
    else:
        return redirect('login')


def update_division(request, id):
    if request.user.is_authenticated:
        devision_obj = get_object_or_404(Division, id=id)
        context = {
            "division": devision_obj,
            'isact_location': 'active'
        }
        if request.method == "POST":
            devision_obj.division_name = request.POST.get("division")
            devision_obj.save()
            messages.success(request, "Division Name Update Successfully")
            return redirect(add_division)
        return render(request, "update/update_division.html", context)
    else:
        return redirect('login')


def remove_division(request, id):
    obj = get_object_or_404(Division, id=id)
    obj.delete()
    messages.success(request, "Division Removed Successfully")
    return redirect(add_division)


def add_service_category(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            service_category = request.POST.get("service_category")
            service_category_obj = ServiceCategory(name=service_category)
            service_category_obj.save()
            messages.success(request, "Service Category Added Successfully")

        service_category_list = ServiceCategory.objects.all()[::-1]
        context = {
            'isact_service_category': 'active',
            'service_category_list': service_category_list
        }
        return render(request, "add/add_service_category.html", context)
    else:
        return redirect('login')


def update_service_category(request, id):
    if request.user.is_authenticated:
        service_category_obj = get_object_or_404(ServiceCategory, id=id)

        context = {
            "service_category": service_category_obj,
            'isact_service_category': 'active'
        }

        if request.method == "POST":
            service_category_obj.name = request.POST.get("service_category")
            service_category_obj.save()
            messages.success(request, "Service Category Updated Successfully")

        return render(request, "update/update_service_category.html", context)
    else:
        return redirect('login')


def delete_service_category(request, id):
    service_category_obj = get_object_or_404(ServiceCategory, id=id)
    service_category_obj.delete()
    messages.success(request, "Service Category Removed Successfully")
    return redirect(add_service_category)


def add_package(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            package = request.POST.get("package")
            service_category_id = request.POST.get("service_category_id")
            package_obj = Package(service_category_id=service_category_id, name=package)
            package_obj.save()
            messages.success(request, "Package Added Successfully")

        service_category_list = ServiceCategory.objects.all()
        package_list = Package.objects.all()[::-1]
        context = {
            'isact_package': 'active',
            'package_list': package_list,
            'service_category_list': service_category_list

        }
        return render(request, "add/add_package.html", context)
    else:
        return redirect('login')


def update_package(request, id):
    if request.user.is_authenticated:
        service_category_list = ServiceCategory.objects.all()
        package_obj = get_object_or_404(Package, id=id)

        context = {
            'service_category_list': service_category_list,
            'package': package_obj,
            'isact_package': 'active'
        }

        if request.method == "POST":
            package_obj.service_category_id = request.POST.get("service_category_id")
            package_obj.name = request.POST.get("package")
            package_obj.save()
            messages.success(request, "Package Updated Successfully")

        return render(request, "update/update_package.html", context)
    else:
        return redirect('login')


def delete_package(request, id):
    package_obj = get_object_or_404(Package, id=id)
    package_obj.delete()
    messages.success(request, "Package Removed Successfully")
    return redirect(add_package)






