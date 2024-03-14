


def btn_language_msg(contact):
    return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{contact}",
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                "text": "Select your preferred language",
                },
                "action": {
                "buttons": [
                    {
                    "type": "reply",
                    "reply": {
                        "id": "lang_English",
                        "title": "English"
                    }
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "lang_Hindi",
                        "title": "Hindi"
                    }
                    }
                ]
                }
            }
            }

def btn_pg_flat_choice(contact):
    return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{contact}",
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                "text": "What type of property are you looking for?",
                },
                "action": {
                "buttons": [
                    {
                    "type": "reply",
                    "reply": {
                        "id": "property_pg",
                        "title": "PG (Paying Guest)"
                    }
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "property_flat",
                        "title": "Flat"
                    }
                    }
                ]
                }
            }
            }


def gender_choice_message(contact):
    return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{contact}",
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                "text": "Select your gender?",
                },
                "action": {
                "buttons": [
                    {
                    "type": "reply",
                    "reply": {
                        "id": "gender_male",
                        "title": "Male"
                    }
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "gender_female",
                        "title": "Female"
                    }
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "gender_main-menu",
                        "title": "Go to Main Menu"
                    }
                    }
                ]
                }
            }
            }

def sharing_choice_message(contact):
    return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{contact}",
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                "text": "Select what type of PG?",
                },
                "action": {
                "buttons": [
                    {
                    "type": "reply",
                    "reply": {
                        "id": "sharing_yes",
                        "title": "Sharing"
                    }
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "sharing_no",
                        "title": "Non sharing"
                    }
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "sharing_main-menu",
                        "title": "Go to Main Menu"
                    }
                    }
                ]
                }
            }
            }
    
def food_choice_message(contact):
    return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{contact}",
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                "text": "Food Preference: ",
                },
                "action": {
                "buttons": [
                    {
                    "type": "reply",
                    "reply": {
                        "id": "food_yes",
                        "title": "With Food"
                    }
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "food_no",
                        "title": "Without Food"
                    }
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "food_main-menu",
                        "title": "Go to Main Menu"
                    }
                    }
                ]
                }
            }
            }
    
def budget_choice_message(contact,food):
    if food=="yes":
        return {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": contact,
  "type": "interactive",
  "interactive": {
    "type": "list",
    "body": {
      "text": "Select your Budget:"
    },
    "action": {
      "button": "Budget",
      "sections": [
        {
          "title": "Budget",
          "rows": [
            {
              "id": "budget_10000-12000",
              "title": "10000-12000"
            },
            {
              "id": "budget_12000-14000",
              "title": "12000-14000"
            },
            {
              "id": "budget_14000-16000",
              "title": "14000-16000"
            },
            {
              "id": "budget_unlimited",
              "title": "No Buget issue",
              "description":"Just want a good quality of place."
            },
            {
              "id": "budget_back",
              "title": "Go to previous menu"
            },
            {
              "id": "budget_main-menu",
              "title": "Go to Main Menu"
            }
          ]
        }
          ]
        }
    }
  }
    else:
        return {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": contact,
  "type": "interactive",
  "interactive": {
    "type": "list",
    "body": {
      "text": "Select your Budget:"
    },
    "action": {
      "button": "Budget",
      "sections": [
        {
          "title": "Budget",
          "rows": [
              {
              "id": "budget_8000-10000",
              "title": "8000-10000"
            },
            {
              "id": "budget_10000-12000",
              "title": "10000-12000"
            },
            {
              "id": "budget_12000-14000",
              "title": "12000-14000"
            },
            {
              "id": "budget_14000-16000",
              "title": "14000-16000"
            },
            {
              "id": "budget_unlimited",
              "title": "No Buget issue",
              "description":"Just want a good quality of place."
            },
            {
              "id": "budget_back",
              "title": "Go to previous menu"
            },
            {
              "id": "budget_main-menu",
              "title": "Go to Main Menu"
            }
          ]
        }
          ]
        }
    }
  }


def flat_choice_message(contact):
    return {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": contact,
  "type": "interactive",
  "interactive": {
    "type": "list",
    "body": {
      "text": "Select what kind flat you are looking:"
    },
    "action": {
      "button": "Flat type",
      "sections": [
        {
          "title": "Flats",
          "rows": [
            {
              "id": "flat_1rk",
              "title": "1 room"
            },
            {
              "id": "flat_1bhk",
              "title": "1 BHK"
            },
            {
              "id": "flat_2bhk",
              "title": "2 BHK"
            },
            {
              "id": "flat_3bhk",
              "title": "3 BHK"
            },
            {
              "id": "flat_back",
              "title": "Go to previous menu"
            },
            {
              "id": "flat_main-menu",
              "title": "Go to Main Menu"
            }
          ]
        }
          ]
        }
    }
  }

def people_choice_message(contact):
    return {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": contact,
  "type": "interactive",
  "interactive": {
    "type": "list",
    "body": {
      "text": "How many person you will be living with :"
    },
    "action": {
      "button": "No of Person",
      "sections": [
        {
          "title": "Person",
          "rows": [
            {
              "id": "person_family",
              "title": "With family"
            },
            {
              "id": "person_1",
              "title": "1 Bachelor"
            },
            {
              "id": "person_2",
              "title": "2 Bachelors"
            },
            {
              "id": "person_3",
              "title": "3 Bachelors"
            },
            {
              "id": "person_4",
              "title": "4 Bachelors"
            },
            {
              "id": "person_5",
              "title": "5 Bachelors"
            },
            {
              "id": "person_back",
              "title": "Go to previous menu"
            },
            {
              "id": "person_main-menu",
              "title": "Go to Main Menu"
            }
          ]
        }
          ]
        }
    }
  }


def furnished_choice_message(contact):
    return {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{contact}",
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                "text": "What type of flat : ",
                },
                "action": {
                "buttons": [
                    {
                    "type": "reply",
                    "reply": {
                        "id": "furnished_semi",
                        "title": "Semi-Furnished"
                    }
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "furnished_full",
                        "title": "Fully-Furnished"
                    },
                    
                    },
                    {
                    "type": "reply",
                    "reply": {
                        "id": "furnished_no",
                        "title": "Un-Furnished"
                    },
                    
                    }
                ]
                }
            }
            }

def flat_budget_choice_message(contact,flat):
    if flat=="no":
        return {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": contact,
  "type": "interactive",
  "interactive": {
    "type": "list",
    "body": {
      "text": "Select your Budget:"
    },
    "action": {
      "button": "Budget",
      "sections": [
        {
          "title": "Budget",
          "rows": [
              {
              "id": "budget_8000-10000",
              "title": "8000-10000"
            },
            {
              "id": "budget_10000-12000",
              "title": "10000-12000"
            },
            {
              "id": "budget_12000-15000",
              "title": "12000-15000"
            },
            {
              "id": "budget_15000-20000",
              "title": "15000-20000"
            },
            {
              "id": "budget_unlimited",
              "title": "No Buget issue",
              "description":"Just want a good quality of place."
            },
            {
              "id": "budget_back",
              "title": "Go to previous menu"
            },
            {
              "id": "budget_main-menu",
              "title": "Go to Main Menu"
            }
          ]
        }
          ]
        }
    }
  }
    else:
        return {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": contact,
  "type": "interactive",
  "interactive": {
    "type": "list",
    "body": {
      "text": "Select your Budget:"
    },
    "action": {
      "button": "Budget",
      "sections": [
        {
          "title": "Budget",
          "rows": [
            {
              "id": "budget_10000-12000",
              "title": "10000-12000"
            },
            {
              "id": "budget_12000-15000",
              "title": "12000-15000"
            },
            {
              "id": "budget_15000-20000",
              "title": "15000-20000"
            },
            {
              "id": "budget_unlimited",
              "title": "No Buget issue",
              "description":"Just want a good quality of place."
            },
            {
              "id": "budget_back",
              "title": "Go to previous menu"
            },
            {
              "id": "budget_main-menu",
              "title": "Go to Main Menu"
            }
          ]
        }
          ]
        }
    }
  }