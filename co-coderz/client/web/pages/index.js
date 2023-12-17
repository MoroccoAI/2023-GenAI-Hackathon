import React from 'react';

const ComingSoonPage = () => {
  const releaseDate = new Date(); // Assuming today is the release date
  releaseDate.setMonth(releaseDate.getMonth() + 1); // Adding 1 month to the release date

  const redirectToBetaPage = () => {
    window.location.href = 'https://hyprsol.com/beta';
  };

  const redirectToYouTube = (url) => {
    window.location.href = url;
  };

  return (
    <div className="coming-soon-container">
      <main className="flex-1 flex flex-col items-center justify-center text-center">
        <img src="/logo/logo-wide-cropped.png" alt="Logo" className="h-20" />
        <div className="mt-8">
          <button
            className="bg-pink-500 hover:bg-rose-700 text-white font-bold py-2 px-4 rounded mr-4"
            onClick={redirectToBetaPage} // Update the onClick handler
          >
            Try Beta
          </button>
          <button
            className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
            onClick={() => redirectToYouTube('https://youtu.be/NBixYx5mOe8')}
          >
            Learn More
          </button>
        </div>
      </main>
    </div>
  );
};

export default ComingSoonPage;
