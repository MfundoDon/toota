import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import logo from '../72dpi_logo_white.jpg';

function Header() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <header className="flex justify-between items-center py-4 px-6 bg-yellow-400 text-black">
      <div className="flex items-center">
        <img src={logo} alt="Toota" className="h-16" />
      </div>
      <nav className="hidden md:flex space-x-4">
        <Link to="/" className="hover:text-primary">Home</Link>
        <Link to="/about" className="hover:text-primary">About Us</Link>
        <Link to="/become-driver" className="hover:text-primary">Become a Driver</Link>
      </nav>
      <div className="flex items-center md:space-x-4">
        <Link to="/login/user" className="px-4 py-2 rounded-md bg-transparent text-white border border-white hover:bg-white hover:text-black transition-colors duration-300"> {/* Changed classes to match the signup button */}
          Login
        </Link>
        <Link to="/signup/user" className="px-4 py-2 rounded-md bg-white text-black border border-white hover:bg-black hover:text-white transition-colors duration-300"> {/* Applied classes from signup button */}
          Sign Up
        </Link>
        <button onClick={toggleMenu} className="md:hidden focus:outline-none">
          <svg
            className="h-6 w-6 text-gray-700 hover:text-primary"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M4 6H20M4 12H20M4 18H20" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </button>
      </div>
      <nav className={`md:hidden bg-black text-white shadow-md transition-all duration-300 ease-in-out ${isOpen ? 'block' : 'hidden'}`}>
        <ul className="py-2 px-4 space-y-2">
          <li>
            <Link to="/" className="hover:text-primary">Home</Link>
          </li>
          <li>
            <Link to="/about" className="hover:text-primary">About Us</Link>
          </li>
          <li>
            <Link to="/become-driver" className="hover:text-primary">Become a Driver</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;

