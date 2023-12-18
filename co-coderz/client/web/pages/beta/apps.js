import React, { useState } from 'react';
import jsonData from '@/public/locales/en/software.json';
import { FaStar } from 'react-icons/fa'; // Importing star icon from react-icons/fa

const itemsPerPage = 6;

const allCategories = [
  'Analytics',
  'Archiving and Digital Preservation (DP)',
  'Automation',
  'Backup',
  'Blogging Platforms',
  'Booking and Scheduling',
  'Bookmarks and Link Sharing',
  'Calendar & Contacts',
  'Communication - Custom Communication Systems',
  'Communication - Email - Complete Solutions',
  'Communication - Email - Mail Delivery Agents',
  'Communication - Email - Mail Transfer Agents',
  'Communication - Email - Mailing Lists and Newsletters',
  'Communication - Email - Webmail Clients',
  'Communication - IRC',
  'Communication - SIP',
  'Communication - Social Networks and Forums',
  'Communication - Video Conferencing',
  'Communication - XMPP - Servers',
  'Communication - XMPP - Web Clients',
  'Community-Supported Agriculture (CSA)',
  'Conference Management',
  'Content Management Systems (CMS)',
  'Database Management',
  'DNS',
  'Document Management - E-books',
  'Document Management - Institutional Repository and Digital Library Software',
  'Document Management - Integrated Library Systems (ILS)',
  'Document Management',
  'E-commerce',
  'Federated Identity & Authentication',
  'Feed Readers',
  'File Transfer - Distributed Filesystems',
  'File Transfer - Object Storage & File Servers',
  'File Transfer - Peer-to-peer Filesharing',
  'File Transfer - Single-click & Drag-n-drop Upload',
  'File Transfer - Web-based File Managers',
  'File Transfer & Synchronization',
  'Games - Administrative Utilities & Control Panels',
  'Games',
  'Genealogy',
  'Groupware',
  'Human Resources Management (HRM)',
  'Internet of Things (IoT)',
  'Inventory Management',
  'Knowledge Management Tools',
  'Learning and Courses',
  'Manufacturing',
  'Maps and Global Positioning System (GPS)',
  'Media Streaming - Audio Streaming',
  'Media Streaming - Multimedia Streaming',
  'Media Streaming - Video Streaming',
  'Media Streaming',
  'Miscellaneous',
  'Money, Budgeting & Management',
  'Monitoring',
  'Note-taking & Editors',
  'Office Suites',
  'Password Managers',
  'Pastebins',
  'Personal Dashboards',
  'Photo and Video Galleries',
  'Polls and Events',
  'Proxy',
  'Recipe Management',
  'Remote Access',
  'Resource Planning',
  'Search Engines',
  'Self-hosting Solutions',
  'Software Development - API Management',
  'Software Development - Continuous Integration & Deployment',
  'Software Development - FaaS & Serverless',
  'Software Development - IDE & Tools',
  'Software Development - Localization',
  'Software Development - Low Code',
  'Software Development - Project Management',
  'Software Development - Testing',
  'Software Development',
  'Static Site Generators',
  'Status / Uptime pages',
  'Task Management & To-do Lists',
  'Ticketing',
  'Time Tracking',
  'URL Shorteners',
  'Video Surveillance',
  'VPN',
  'Web Servers',
  'Wikis'
];

const AppsPage = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedApp, setSelectedApp] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategories, setSelectedCategories] = useState([]);

  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;

  const filteredData = jsonData.filter((app) => {
    const matchesSearch = app.name.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesCategories =
      selectedCategories.length === 0 || selectedCategories.some((category) => app.tags.includes(category));
    return matchesSearch && matchesCategories;
  });

  const currentData = filteredData.slice(startIndex, endIndex);

  const totalPages = Math.ceil(filteredData.length / itemsPerPage);

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage);
    setSelectedApp(null);
  };

  const handleAppClick = (app) => {
    setSelectedApp(app);
  };

  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
    setCurrentPage(1);
  };

  const handleCategoryChange = (category) => {
    if (selectedCategories.includes(category)) {
      setSelectedCategories(selectedCategories.filter((c) => c !== category));
    } else {
      setSelectedCategories([...selectedCategories, category]);
    }
    setCurrentPage(1);
  };

  const handleCloseModal = () => {
    setSelectedApp(null);
  };

  return (
    <div className="bg-violet-100 p-8 mx-auto rounded">
      <h1 className="text-4xl font-bold mb-8">Apps Page</h1>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Search by name"
          value={searchQuery}
          onChange={handleSearchChange}
          className="border border-gray-300 p-2 rounded"
        />
      </div>
      <div className="flex flex-wrap mb-4">
        {allCategories.map((category) => (
          <span key={category} className="mr-2 mb-2">
            <button
              onClick={() => handleCategoryChange(category)}
              className={`bg-violet-500 text-white px-4 py-2 rounded ${
                selectedCategories.includes(category) ? 'bg-opacity-75' : ''
              }`}
            >
              {category}
            </button>
          </span>
        ))}
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        {currentData.map((app, index) => (
          <div
            key={index}
            className={`bg-white p-6 rounded shadow-md transition-transform transform hover:scale-105 cursor-pointer ${
              selectedApp && selectedApp.name === app.name ? 'border border-violet-500' : ''
            }`}
            onClick={() => handleAppClick(app)}
          >
            <h3 className="text-xl font-semibold mb-3">{app.name}</h3>
            <div className="flex items-center mb-4">
              <FaStar className="text-yellow-500 mr-1" />
              <span>{app.stargazers_count}</span>
            </div>
            <a
              href={app.website_url}
              className="text-violet-500 hover:underline"
              target="_blank"
              rel="noopener noreferrer"
            >
              Learn more
            </a>
          </div>
        ))}
      </div>
      <div className="flex justify-between mt-8">
        <button
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1}
          className="bg-violet-500 text-white px-4 py-2 rounded transition-transform transform hover:scale-105"
        >
          Previous Page
        </button>
        <span className="text-gray-600">
          Page {currentPage} of {totalPages}
        </span>
        <button
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
          className="bg-violet-500 text-white px-4 py-2 rounded transition-transform transform hover:scale-105"
        >
          Next Page
        </button>
      </div>
      {selectedApp && (
        <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center">
          <div className="bg-white p-8 rounded shadow-lg max-w-screen-md w-full">
            <h2 className="text-2xl font-bold mb-4">{selectedApp.name}</h2>
            <p className="text-gray-600 mb-4">{selectedApp.description}</p>
            {/* Add more details as needed */}
            <button
              onClick={handleCloseModal}
              className="bg-violet-500 text-white px-4 py-2 rounded transition-transform transform hover:scale-105"
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default AppsPage;
