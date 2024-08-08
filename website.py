import streamlit as st
import search

st.title('Ticket Finder')
input_results = st.text_input("Please enter a concert or event you're looking for tickets to", value="")

if input_results:
    results = search.getResults(input_results)["_embedded"]
    for event in results["events"]:
        if "url" not in event:
            continue
        st.write(event["name"])
        st.write(event["url"])
        st.write(event["dates"]["start"]["localDate"] + " at " + event["dates"]["start"]["localTime"])
        
    