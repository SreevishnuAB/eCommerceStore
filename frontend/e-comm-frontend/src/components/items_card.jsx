import { useState } from 'react';


function ItemCard({ item, handleItemCounter }){

    const [quantity, setQuantity] = useState(item.quantity);
    return (
        <div className="card">
            <h2>{item.itemName}</h2>
            <h3>{item.price}</h3>

        </div>
    );
}