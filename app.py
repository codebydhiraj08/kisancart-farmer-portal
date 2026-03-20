from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime, timedelta

app = Flask(__name__, static_url_path='', static_folder='.')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kisancart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Indian Standard Time (IST) set karne ka function
def get_ist_time():
    return datetime.utcnow() + timedelta(hours=5, minutes=30)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(20), unique=True)
    customer_name = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    address = db.Column(db.String(255))
    total_amount = db.Column(db.Float)
    items = db.Column(db.Text) 
    date = db.Column(db.DateTime, default=get_ist_time) # Yahan India ka time aayega

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/place-order', methods=['POST'])
def place_order():
    data = request.json
    new_order = Order(
        order_id=data['order_id'],
        customer_name=data.get('customer_name', 'Unknown'),
        phone=data.get('phone', 'Unknown'),
        address=data.get('address', 'Unknown'),
        total_amount=data['total_amount'],
        items=json.dumps(data['items'])
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order database me save ho gaya!", "status": "success"})

# NAYA: Order Delete karne ka rasta
@app.route('/admin/delete-order/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({"status": "success"})
    return jsonify({"status": "error"})

@app.route('/admin/orders')
def view_orders():
    orders = Order.query.order_by(Order.date.desc()).all()
    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="30"> <title>KisanCart - Owner Dashboard</title>
        <script src="https://cdn.tailwindcss.com/3.4.17"></script>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        <style>body { font-family: 'Poppins', sans-serif; }</style>
        
        <script>
            function deleteOrder(id, btnElement) {
                // Button ko loading animation me dalo
                btnElement.innerHTML = '<i class="fa-solid fa-spinner fa-spin mr-1"></i> Deleting...';
                btnElement.disabled = true;
                
                fetch('/admin/delete-order/' + id, { method: 'POST' })
                .then(res => res.json())
                .then(data => { 
                    if(data.status === 'success') {
                        // Card ko smoothly chota karke gayab karo
                        const card = btnElement.closest('.order-card');
                        card.style.transition = "all 0.4s ease";
                        card.style.opacity = "0";
                        card.style.transform = "scale(0.9)";
                        
                        setTimeout(() => {
                            card.remove();
                            // Agar screen pe saare order delete ho gaye, to page refresh kar do
                            if(document.querySelectorAll('.order-card').length === 0) location.reload();
                        }, 400);
                    }
                });
            }
        </script>
    </head>
    <body class="bg-gray-50 min-h-screen">
        <nav class="bg-gray-900 text-white shadow-xl sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 bg-gradient-to-r from-emerald-500 to-cyan-500 rounded-lg flex items-center justify-center text-xl shadow-lg">
                        <i class="fa-solid fa-chart-pie"></i>
                    </div>
                    <h1 class="font-extrabold text-2xl tracking-tight">Admin<span class="text-emerald-400">Panel</span></h1>
                </div>
                <div class="flex items-center gap-4">
                    <span class="bg-gray-800 px-4 py-2 rounded-full text-sm font-bold border border-gray-700 shadow-inner text-emerald-400">
                        <i class="fa-solid fa-box mr-1"></i> Total Orders: """ + str(len(orders)) + """
                    </span>
                    <a href="/" class="bg-emerald-500 hover:bg-emerald-600 px-5 py-2 rounded-full text-sm font-bold transition shadow-lg flex items-center gap-2">
                        Live Shop <i class="fa-solid fa-arrow-up-right-from-square"></i>
                    </a>
                </div>
            </div>
        </nav>
        <div class="max-w-7xl mx-auto px-4 py-10">
    """

    if not orders:
        html += """<div class="text-center py-24 bg-white rounded-3xl shadow-sm border border-gray-100 mt-10"><div class="text-gray-200 text-7xl mb-6"><i class="fa-solid fa-clipboard-list"></i></div><h3 class="text-2xl font-bold text-gray-900 mb-2">Inbox Empty</h3><p class="text-gray-500 font-medium">Your store is waiting for its first customer. Dashboard auto-refreshes.</p></div>"""
    else:
        html += '<div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">'
        for o in orders:
            items_html = ""
            try:
                for item in json.loads(o.items):
                    # FIX: Yahan img src me "/" add kiya hai taaki image sahi jagah se aaye
                    items_html += f"""<div class="flex justify-between items-center bg-gray-50 p-2.5 rounded-lg border border-gray-100 mb-2"><div class="flex items-center gap-2"><div class="w-8 h-8 rounded bg-white border border-gray-200 overflow-hidden flex-shrink-0"><img src="/{item.get('image', '')}" class="w-full h-full object-cover"></div><span class="font-bold text-sm text-gray-800">{item.get('name', 'Item')} <span class="text-emerald-600 text-xs ml-1 bg-emerald-100 px-1.5 py-0.5 rounded">Qty: {item.get('quantity', 1)}</span></span></div><span class="font-extrabold text-sm text-gray-900">Rs. {item.get('price', 0) * item.get('quantity', 1)}</span></div>"""
            except: pass

            # Card me 'order-card' class add ki aur Delete button update kiya
            html += f"""
                <div class="order-card bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                    <div class="bg-gradient-to-r from-emerald-50 to-cyan-50 border-b border-gray-100 px-6 py-4 flex justify-between items-center">
                        <div>
                            <span class="text-[10px] font-bold text-emerald-600 uppercase tracking-widest block mb-1">Order ID</span>
                            <span class="text-lg font-extrabold text-gray-900">#{o.order_id}</span>
                        </div>
                        <div class="text-right">
                            <button onclick="deleteOrder({o.id}, this)" class="bg-red-100 text-red-600 hover:bg-red-500 hover:text-white px-3 py-1 rounded text-xs font-bold transition shadow-sm mb-1"><i class="fa-solid fa-trash-can mr-1"></i> Delete</button>
                            <span class="text-xs font-bold text-gray-500 block"><i class="fa-regular fa-clock mr-1"></i> {o.date.strftime('%I:%M %p | %d %b')}</span>
                        </div>
                    </div>
                    <div class="p-6">
                        <div class="flex items-start gap-4 mb-5">
                            <div class="w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center text-gray-500 text-xl flex-shrink-0 shadow-inner"><i class="fa-solid fa-user"></i></div>
                            <div>
                                <h4 class="font-bold text-gray-900 text-lg leading-tight">{o.customer_name}</h4>
                                <p class="text-xs font-bold text-emerald-600 mt-1"><i class="fa-solid fa-phone mr-1"></i> {o.phone}</p>
                                <p class="text-xs font-medium text-gray-500 mt-1.5 leading-relaxed"><i class="fa-solid fa-location-dot text-rose-400 mr-1"></i> {o.address}</p>
                            </div>
                        </div>
                        <div class="border-t border-gray-100 pt-4 mb-4">
                            <div class="max-h-40 overflow-y-auto pr-1 custom-scroll">{items_html}</div>
                        </div>
                        <div class="bg-gray-900 rounded-xl p-4 flex justify-between items-center shadow-md">
                            <span class="text-gray-400 font-medium text-sm">Total Paid</span>
                            <span class="text-2xl font-extrabold text-emerald-400">Rs. {o.total_amount}</span>
                        </div>
                    </div>
                </div>
            """
        html += '</div></div><style>.custom-scroll::-webkit-scrollbar { width: 4px; } .custom-scroll::-webkit-scrollbar-thumb { background: #d1d5db; border-radius: 4px; }</style></body></html>'
    return html

if __name__ == '__main__':
    app.run(debug=True, port=5000)