import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import ProductsPage from './pages/ProductsPage';


function App() {
  return (
    <div>
      <nav>
        <Link to="/">Products</Link> | <Link to="/cart">Cart</Link> | <Link to="/checkout">Checkout</Link>
      </nav>
      <Routes>
        <Route path="/" element={<ProductsPage />} />
    
      </Routes>
    </div>
  );
}

export default App;
