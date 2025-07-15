
# Multi Agent Guidance voice assistant
## Main Features are:
Complete Multi-Agent Voice System: Working implementation with all core features
Web Search RAG Integration: Functional real-time information retrieval using web search APIs
Vector Memory System: Persistent conversation context storage and retrieval
## Description :
The system is an interactive Voice-based assistant designed to respond to user queries using two distinct AI agents:
1.Realist Agent-provides practical , reality based responses.
2.Expert Agent-Offers professional , Knowledge-driven responses.
Additionally, i have used Pinecone Vector Database to store and retrieve past user queries and responses as memory, enabling context-aware assistance.

## WorkFlow:
1.Voice Input:The user speaks his query via the microphone.The listen() function converts this speech into text using SpeechRecognition.

2.Processing by Agents:user query is passed to 

**Realist Agent:** generates a realistic,practical reply.

**Expert Agent:** Provides a knowlwdge based , expert level reponse.

3.Web SEarch RAG :provides up to date information during conversation.

4.Voice output:Each agents reponse is converted into speech.

5.Memory storage:user query and both agent responses are saved as record in pinecone vector database.

6.Memory Retrieval:On further user queries the system checks the pinecone database for similar past records and retrieves relevant information.


## Architecture :
![image](https://github.com/user-attachments/assets/284e24f8-f9a1-47bb-bca8-7fb8db6df407)

The system starts by converting the user's voice input to text using STT module.
The Query Analyzer checks the nature of the query to dicide whether to fetch information from local knowledge or to perform a real-time web search using RAG techniques.
Both the agents responses and web data are merged by final response builder and converted back to speech through TTS system to provide the final response to the user.

## Demo Video:

https://github.com/user-attachments/assets/7fd6da70-075f-4fae-bf04-98df937bd152


In this version, the system utilizes the Realist and Expert Agents to process and summarize the retrieved web search data.After performing a real time web search , the agents intelligently extract, filter and condense the most relevant information, eliminating unnecessary details.This ensures that the final response provided to the user is concise and clear.
