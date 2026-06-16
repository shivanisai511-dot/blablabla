# SPORTSPACE

Deployment-ready Streamlit app.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Flow
Landing Page → Main Menu → Discover Sports → Facilities → Booking → My Bookings

## Notes
- No database required.
- Bookings are stored in `st.session_state` for the active browser session.
- Time selection uses fixed slot buttons/dropdowns instead of `st.time_input` to avoid browser-side React recursion issues in some hosted environments.
