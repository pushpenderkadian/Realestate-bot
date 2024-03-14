import app.utils as utils
import app.message_content as contents

def startflow(msgdata):
    new_user=0
    contact = utils.extract_contact(msgdata)
    if utils.extract_text_message(msgdata):
        message = utils.extract_text_message(msgdata)
        if message.lower() in ["hi","hlo","hello","hey"]:
            utils.send_text_message(contact, "Hello \n\n Welcome to our Living support bot.")
            if utils.check_user(contact):
                utils.set_user_current_step(contact,[1,False])
            else:
                new_user=1
        elif message.lower() in ["/lang","/language"]:
            utils.send_payload_message(contents.btn_language_msg(contact))
            return
    if utils.extract_button_message(msgdata):
        button = utils.extract_button_message(msgdata)
        if "lang_" in button["id"]:
            if button["id"]=="lang_English":
                utils.send_text_message(contact, 'You have selected English as your preferred language.\n\nTo change your language preference, type "/lang" or "/language".')
                utils.set_user_language(contact, "english")
            elif button["id"]=="lang_Hindi":
                utils.send_text_message(contact, 'You have selected Hindi as your preferred language.\n\nTo change your language preference, type "/lang" or "/language".')
                utils.set_user_language(contact, "hindi")
            

    botflow(msgdata,contact,new_user)

def botflow(msgdata,contact,new_user=0):
    if new_user==1:
        utils.send_payload_message(contents.btn_language_msg(contact))
        if utils.get_user_current_step(contact)== 0:
            utils.set_user_current_step(contact,[1,False])
    else:
        current_step = utils.get_user_current_step(contact)
        if current_step[0]== 1 :
            choice_selection_step(contact,msgdata)
        elif current_step[0]== 2:
            user_requirement=utils.get_user_requirements(contact)
            if user_requirement=="pg":
                gender_choice(contact,msgdata)
            elif user_requirement=="flat":
                flat_selection(contact,msgdata)
        elif current_step[0]== 3:
            user_requirement=utils.get_user_requirements(contact)
            if user_requirement=="pg":
                sharing_choice(contact,msgdata)
            elif user_requirement=="flat":
                no_people_choice(contact,msgdata)
        elif current_step[0]== 4:
            user_requirement=utils.get_user_requirements(contact)
            if user_requirement=="pg":
                food_choice(contact,msgdata)
            elif user_requirement=="flat":
                furnished_choice(contact,msgdata)
        elif current_step[0]== 5:
            user_requirement=utils.get_user_requirements(contact)
            if user_requirement=="pg":
                budget_choice(contact,msgdata)
            elif user_requirement=="flat":
                flat_budget_choice(contact,msgdata)

def step_update(contact):
    current_step = utils.get_user_current_step(contact)
    utils.set_user_current_step(contact,[current_step[0]+1,False])
           

def choice_selection_step(contact,msgdata,current_step=None):
    current_step = utils.get_user_current_step(contact)
    if current_step[1]== False :
        utils.send_payload_message(contents.btn_pg_flat_choice(contact))
        utils.set_user_current_step(contact,[current_step[0],True])
    elif current_step[1]== True:
        if utils.extract_button_message(msgdata):
            button = utils.extract_button_message(msgdata)
            if "property_" in button["id"]:
                if button["id"]=="property_pg":
                    utils.add_user_requirements(contact, "pg")
                    step_update(contact)
                    gender_choice(contact)
                elif button["id"]=="property_flat":
                    utils.add_user_requirements(contact, "flat")
                    step_update(contact)
                    flat_selection(contact)
            else:
                utils.send_text_message(contact, "Invalid selection. Please try again.")
                utils.send_payload_message(contents.btn_pg_flat_choice(contact))
        else:
            utils.send_text_message(contact, "Invalid selection. Please try again.")
            utils.send_payload_message(contents.btn_pg_flat_choice(contact))



def gender_choice(contact,msgdata=None):
    current_step = utils.get_user_current_step(contact)
    if current_step[1]== False and msgdata==None:
        utils.send_payload_message(contents.gender_choice_message(contact))
        utils.set_user_current_step(contact,[current_step[0],True])
    elif current_step[1]== True:
        if utils.extract_button_message(msgdata):
            button = utils.extract_button_message(msgdata)
            if "gender_" in button["id"]:
                if button["id"]=="gender_male":
                    utils.add_user_requirements_pg(contact,"gender","male")
                    step_update(contact)
                    
                elif button["id"]=="gender_female":
                    utils.add_user_requirements_pg(contact,"gender","female")
                    step_update(contact)
                elif button["id"]=="gender_main-menu":
                    utils.set_user_current_step(contact,[1,False])
                    choice_selection_step(contact,msgdata)
                    return
                sharing_choice(contact)
            else:
                utils.send_text_message(contact, "Invalid selection. Please try again.")
                utils.send_payload_message(contents.gender_choice_message(contact))
        else:
            utils.send_text_message(contact, "Invalid selection. Please try again.")
            utils.send_payload_message(contents.gender_choice_message(contact))

def sharing_choice(contact,msgdata=None):
    current_step = utils.get_user_current_step(contact)
    if current_step[1]== False and msgdata==None:
        utils.send_payload_message(contents.sharing_choice_message(contact))
        utils.set_user_current_step(contact,[current_step[0],True])
    elif current_step[1]== True:
        if utils.extract_button_message(msgdata):
            button = utils.extract_button_message(msgdata)
            if "sharing_" in button["id"]:
                if button["id"]=="sharing_yes":
                    utils.add_user_requirements_pg(contact,"sharing","yes")
                    step_update(contact)
                    
                elif button["id"]=="sharing_no":
                    utils.add_user_requirements_pg(contact,"sharing","no")
                    step_update(contact)
                elif button["id"]=="sharing_main-menu":
                    utils.set_user_current_step(contact,[1,False])
                    choice_selection_step(contact,msgdata)
                    return
                food_choice(contact)
            else:
                utils.send_text_message(contact, "Invalid selection. Please try again.")
                utils.send_payload_message(contents.sharing_choice_message(contact))
        else:
            utils.send_text_message(contact, "Invalid selection. Please try again.")
            utils.send_payload_message(contents.sharing_choice_message(contact))

def food_choice(contact,msgdata=None):
    current_step = utils.get_user_current_step(contact)
    if current_step[1]== False and msgdata==None:
        utils.send_payload_message(contents.food_choice_message(contact))
        utils.set_user_current_step(contact,[current_step[0],True])
    elif current_step[1]== True:
        if utils.extract_button_message(msgdata):
            button = utils.extract_button_message(msgdata)
            if "food_" in button["id"]:
                if button["id"]=="food_yes":
                    utils.add_user_requirements_pg(contact,"food","yes")
                    step_update(contact)
                    
                elif button["id"]=="food_no":
                    utils.add_user_requirements_pg(contact,"food","no")
                    step_update(contact)
                elif button["id"]=="food_main-menu":
                    utils.set_user_current_step(contact,[1,False])
                    choice_selection_step(contact,msgdata)
                    return
                budget_choice(contact)
            else:
                utils.send_text_message(contact, "Invalid selection. Please try again.")
                utils.send_payload_message(contents.food_choice_message(contact))
        else:
            utils.send_text_message(contact, "Invalid selection. Please try again.")
            utils.send_payload_message(contents.food_choice_message(contact))

def budget_choice(contact,msgdata=None):
    current_step = utils.get_user_current_step(contact)
    if current_step[1]== False and msgdata==None:
        utils.send_payload_message(contents.budget_choice_message(contact,utils.get_user_requirements_pg(contact,"food")))
        utils.set_user_current_step(contact,[current_step[0],True])
    elif current_step[1]== True:
        if utils.extract_list_reply(msgdata):
            list = utils.extract_list_reply(msgdata)
            if "budget_" in list["id"]:
                if list["id"]=="budget_main-menu":
                    utils.set_user_current_step(contact,[1,False])
                    choice_selection_step(contact,msgdata)
                    return
                elif list["id"]=="budget_back":
                    utils.set_user_current_step(contact,[current_step[0]-1,False])
                    food_choice(contact)
                    return
                budget=list["id"].split("_")[1]
                utils.add_user_requirements_pg(contact,"budget",budget)
                step_update(contact)                   
                
                finish(contact)
            else:
                utils.send_text_message(contact, "Invalid selection. Please try again.")
                utils.send_payload_message(contents.budget_choice_message(contact,utils.get_user_requirements_pg(contact,"food")))
        else:
            utils.send_text_message(contact, "Invalid selection. Please try again.")
            utils.send_payload_message(contents.budget_choice_message(contact,utils.get_user_requirements_pg(contact,"food")))

def finish(contact,msgdata=None):
    utils.send_text_message(contact,"Thanks for considering us.\n\nWe will contact you soon with some good findings as per your requirement.")
    utils.complete_flow(contact)


    

def flat_selection(contact,msgdata=None):
    current_step = utils.get_user_current_step(contact)
    if current_step[1]== False and msgdata==None:
        utils.send_payload_message(contents.flat_choice_message(contact))
        utils.set_user_current_step(contact,[current_step[0],True])
    elif current_step[1]== True:
        if utils.extract_list_reply(msgdata):
            button = utils.extract_list_reply(msgdata)
            if "flat_" in button["id"]:
                if button["id"]=="flat_main-menu":
                    utils.set_user_current_step(contact,[1,False])
                    choice_selection_step(contact,msgdata)
                    return
                elif button["id"]=="flat_back":
                    utils.set_user_current_step(contact,[current_step[0]-1,False])
                    choice_selection_step(contact,msgdata)
                    return
                flat_type=button["id"].split("_")[1]
                utils.add_user_requirements_flat(contact,"flat_type",flat_type)
                step_update(contact)

                no_people_choice(contact)
            else:
                utils.send_text_message(contact, "Invalid selection. Please try again.")
                utils.send_payload_message(contents.flat_choice_message(contact))
        else:
            utils.send_text_message(contact, "Invalid selection. Please try again.")
            utils.send_payload_message(contents.flat_choice_message(contact))

def no_people_choice(contact,msgdata=None):
    current_step = utils.get_user_current_step(contact)
    if current_step[1]== False and msgdata==None:
        utils.send_payload_message(contents.people_choice_message(contact))
        utils.set_user_current_step(contact,[current_step[0],True])
    elif current_step[1]== True:
        if utils.extract_list_reply(msgdata):
            button = utils.extract_list_reply(msgdata)
            if "person_" in button["id"]:
                if button["id"]=="person_main-menu":
                    utils.set_user_current_step(contact,[1,False])
                    choice_selection_step(contact,msgdata)
                    return
                elif button["id"]=="person_back":
                    utils.set_user_current_step(contact,[current_step[0]-1,False])
                    flat_selection(contact)
                    return
                flat_type=button["id"].split("_")[1]
                print(flat_type)
                utils.add_user_requirements_flat(contact,"persons",flat_type)
                step_update(contact)

                furnished_choice(contact)
            else:
                utils.send_text_message(contact, "Invalid selection. Please try again.")
                utils.send_payload_message(contents.people_choice_message(contact))
        else:
            utils.send_text_message(contact, "Invalid selection. Please try again.")
            utils.send_payload_message(contents.people_choice_message(contact))

def furnished_choice(contact,msgdata=None):
    current_step = utils.get_user_current_step(contact)
    if current_step[1]== False and msgdata==None:
        utils.send_payload_message(contents.furnished_choice_message(contact))
        utils.set_user_current_step(contact,[current_step[0],True])
    elif current_step[1]== True:
        if utils.extract_button_message(msgdata):
            button = utils.extract_button_message(msgdata)
            if "furnished_" in button["id"]:
                if button["id"]=="furnished_semi":
                    utils.add_user_requirements_flat(contact,"furnished","semi")
                    step_update(contact)
                    
                elif button["id"]=="furnished_full":
                    utils.add_user_requirements_flat(contact,"furnished","full")
                    step_update(contact)
                elif button["id"]=="furnished_no":
                    utils.add_user_requirements_flat(contact,"furnished","unfurnished")
                    step_update(contact)
                
                flat_budget_choice(contact)
            else:
                utils.send_text_message(contact, "Invalid selection. Please try again.")
                utils.send_payload_message(contents.furnished_choice_message(contact))
        else:
            utils.send_text_message(contact, "Invalid selection. Please try again.")
            utils.send_payload_message(contents.furnished_choice_message(contact))

def flat_budget_choice(contact,msgdata=None):
    current_step = utils.get_user_current_step(contact)
    if current_step[1]== False and msgdata==None:
        utils.send_payload_message(contents.flat_budget_choice_message(contact,utils.get_user_requirements_flat(contact,"furnished")))
        utils.set_user_current_step(contact,[current_step[0],True])
    elif current_step[1]== True:
        if utils.extract_list_reply(msgdata):
            list = utils.extract_list_reply(msgdata)
            if "budget_" in list["id"]:
                if list["id"]=="budget_main-menu":
                    utils.set_user_current_step(contact,[1,False])
                    choice_selection_step(contact,msgdata)
                    return
                elif list["id"]=="budget_back":
                    utils.set_user_current_step(contact,[current_step[0]-1,False])
                    furnished_choice(contact)
                    return
                budget=list["id"].split("_")[1]
                utils.add_user_requirements_flat(contact,"budget",budget)
                step_update(contact)                   
                finish(contact)
            else:
                utils.send_text_message(contact, "Invalid selection. Please try again.")
                utils.send_payload_message(contents.flat_budget_choice_message(contact,utils.get_user_requirements_flat(contact,"furnished")))
        else:
            utils.send_text_message(contact, "Invalid selection. Please try again.")
            utils.send_payload_message(contents.flat_budget_choice_message(contact,utils.get_user_requirements_flat(contact,"furnished")))



    

