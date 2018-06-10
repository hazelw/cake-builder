import sqllite3

sqllite_file = './cakes.db'

def load_real_cakes():
    conn = sqllite3.connect(sqllite_file)
    c = conn.cursor()
