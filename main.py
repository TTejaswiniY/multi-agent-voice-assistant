from agents import realist_agent,expert_agent
from memory import add_to_memory, search_memory
from voice import listen,speak
def main():
    speak("Hello !! What would you like to discuss today ?")
    user=listen()
    print("user said:",user)
    realist_reply=realist_agent(user)
    print("Realist Agent:",realist_reply)
    speak(realist_reply)
    expert_reply=expert_agent(user,topic="career guidance")
    print("Expert agent:",expert_reply)
    speak(expert_reply)
    add_to_memory(user,realist_reply+" "+expert_reply)
    speak("Do you have any more questions?")
    user2=listen()
    print("user said:",user)
    realist_reply2=realist_agent(user)
    print("Realist Agent:",realist_reply2)
    speak(realist_reply2)
    expert_reply2=expert_agent(user2,topic="career guidance")
    print("Expert agent:",expert_reply2)
    speak(expert_reply2)
    add_to_memory(user2,realist_reply2+" "+expert_reply2)
    past = search_memory(user2)
    print("Memory Retrieved:", past)

if __name__=="__main__":
    main()