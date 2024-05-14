import React, { useState, useEffect } from 'react';
import { BellIcon, UserIcon, CogIcon, ClockIcon, CurrencyDollarIcon, ClipboardCheckIcon } from '@heroicons/react/outline'; // Import required icons
import { useNavigate } from 'react-router-dom';
import LogoutConfirmationForm from './LogoutConfirmationForm'; // Import the LogoutConfirmationForm component
import DriverProfileForm from "./DriverProfile";
import { ToastContainer, toast } from 'react-toastify';
import supabase from '../../services/SupaBaseClient';
import { getDriver, getAccessToken } from "../../services/AuthService";

const DriverDashboard = () => {
  const navigate = useNavigate();
  const [showLogoutConfirmation, setShowLogoutConfirmation] = useState(false);
  const [editingProfile, setEditingProfile] = useState(false); // State variable to track profile editing mode
  const [verified, setVerified] = useState(false);
  const token = getAccessToken();

  useEffect(() => {
    const fetchVerificationStatus = async () => {
      try {
        if (token) {
          const driver = await getDriver();
          const response = await fetch(`http://127.0.0.1:8000/api/driver/verification-check/${driver.id}/`, {
            method: 'GET',
            headers: {
              'Authorization': `Bearer ${token}`,
            },
          });
          const data = await response.json();
          const { verified } = data;
          setVerified(verified);
        }
      } catch (error) {
        console.error('Error fetching verification status:', error);
      }
    };

    fetchVerificationStatus();
  }, [token]);

  useEffect(() => {
    if (!verified) {
      navigate('/driver-verification-documents');
    }
  }, [verified, navigate]);

  const handleLogout = () => {
    setShowLogoutConfirmation(true);
  };

  const handleLogoutConfirmation = (confirmLogout) => {
    if (confirmLogout) {
      // Perform logout action
      // Redirect to login/driver route
      navigate('/login/driver');
    } else {
      setShowLogoutConfirmation(false);
    }
  };

  // Function to toggle profile editing mode
  const toggleEditingProfile = () => {
    setEditingProfile(prevEditingProfile => !prevEditingProfile);
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
     
      {/* Main Content */}
      <main className="container mx-auto px-8 py-6">
        {/* Dashboard Navigation */}

        {/* Sections */}
        {editingProfile ? ( // Conditionally render profile form if editingProfile is true
          <DriverProfileForm onCancel={toggleEditingProfile} /> // Pass onCancel prop to handle canceling profile editing
        ) : (
          <section className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Render other sections here */}
            <DashboardSection icon={<ClockIcon className="h-8 w-8" />} title="Ongoing Rides" />
            <DashboardSection icon={<CurrencyDollarIcon className="h-8 w-8" />} title="Earnings and Statistics" />
            <DashboardSection icon={<ClipboardCheckIcon className="h-8 w-8" />} title="Ride History" />
            <DashboardSection icon={<CogIcon className="h-8 w-8" />} title="Settings and Support" />
          </section>
        )}
      </main>

      {/* Render LogoutConfirmationForm if showLogoutConfirmation is true */}
      {showLogoutConfirmation && (
        <LogoutConfirmationForm onConfirm={handleLogoutConfirmation} />
      )}
      <ToastContainer 
        autoClose={10000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="light"
        transition: Bounce
      />
    </div>
  );
};

// Component for navigation items
const NavItem = ({ icon, text, handleClick }) => { // Added handleClick prop
  return (
    <div className="flex items-center space-x-2 text-gray-600 hover:text-gray-800 cursor-pointer" onClick={handleClick}> {/* Added onClick event handler */}
      {icon}
      <span className="hidden md:inline">{text}</span>
    </div>
  );
};

// Component for dashboard sections
const DashboardSection = ({ icon, title }) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md flex items-center space-x-4">
      {icon}
      <h2 className="text-lg font-semibold text-gray-800">{title}</h2>
    </div>
  );
};

export default DriverDashboard;

