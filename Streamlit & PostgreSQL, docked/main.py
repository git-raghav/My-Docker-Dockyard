import streamlit as st
import psycopg2

# Custom CSS for better readability
st.markdown("""
    <style>
        body {
            background-color: #f4f6f9;
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #333;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            color: #555;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .card {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            color: #333;
        }
        .data {
            font-size: 18px;
            line-height: 1.6;
        }
        .data span {
            color: #0073e6;
        }
        .error {
            color: #e74c3c;
        }
        .success {
            color: #2ecc71;
        }
        .warning {
            color: #f39c12;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 PostgreSQL Connection with Streamlit through Docker")

DB_HOST = "my_postgres_container"
DB_NAME = "testdb"
DB_USER = "raghav"
DB_PASSWORD = "secret"

def fetch_data():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM passengers;")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        st.error(f"❌ Database connection error: {str(e)}")
        return []

def insert_data(name, location):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO passengers (name, location) VALUES (%s, %s);", (name, location))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("✅ Passenger added successfully!")
        st.experimental_rerun()  # Refresh data automatically
    except Exception as e:
        st.error(f"❌ Error inserting data: {str(e)}")

# Form to add new passengers
st.subheader("➕ Add New Passenger")
name = st.text_input("Name")
location = st.text_input("Location")
if st.button("Add Passenger"):
    if name and location:
        insert_data(name, location)
    else:
        st.warning("⚠️ Please enter both name and location.")

# Display passengers
data = fetch_data()
if data:
    st.subheader("📊 Passenger List")
    for row in data:
        st.markdown(f"""
            <div class="card">
                <p class="data"><strong>🆔 ID:</strong> {row[0]} <br>
                <strong>🏷 Name:</strong> {row[1]} <br>
                <strong>📍 Location:</strong> {row[2]}</p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("⚠️ No data found in the `passengers` table.")
