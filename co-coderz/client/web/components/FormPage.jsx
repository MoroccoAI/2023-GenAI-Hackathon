import React from 'react';

const FormPage = ({ formData, handleInputChange, handleCheckboxChange, handleOtherInputChange, handleSubmit, projectData, children }) => {
  return (
    <div className="bg-violet-100 text-black min-h-screen py-8">
      <div className="max-w-2xl mx-auto bg-white p-8 rounded shadow-md">
        <h1 className="text-2xl font-bold mb-4">Project Submission</h1>
        <form onSubmit={handleSubmit}>
          {projectData.map((question) => (
            <div key={question.id} className="mb-4">
              <label className="block text-gray-700 font-bold mb-2" htmlFor={question.tag}>
                {question.title}
              </label>
              {question.multiple ? (
                <div className="flex flex-wrap">
                  {question.answers.map((answer) => (
                    <button
                      key={answer}
                      type="button"
                      onClick={() =>
                        handleCheckboxChange({
                          target: { name: question.tag, value: answer, checked: !formData[question.tag].includes(answer) },
                        })
                      }
                      className={`mr-2 mb-2 px-4 py-2 rounded ${
                        formData[question.tag].includes(answer)
                          ? 'bg-violet-500 text-white focus:outline-none'
                          : 'bg-gray-300 text-gray-700 hover:bg-gray-400 focus:outline-none'
                      }`}
                      aria-pressed={formData[question.tag].includes(answer)}
                    >
                      {answer}
                    </button>
                  ))}
                </div>
              ) : (
                <div>
                  <select
                    id={question.tag}
                    name={question.tag}
                    value={formData[question.tag]}
                    onChange={handleInputChange}
                    className="block w-full border border-gray-300 rounded p-2 mb-2"
                  >
                    <option value="" disabled hidden>
                      Select
                    </option>
                    {question.answers.map((answer) => (
                      <option key={answer} value={answer}>
                        {answer}
                      </option>
                    ))}
                  </select>
                  {question.answers.includes('Other') && formData[question.tag] === 'Other' && (
                    <input
                      type="text"
                      placeholder="Please specify..."
                      name={`${question.tag}_other`}
                      value={formData[`${question.tag}_other`] || ''}
                      onChange={handleOtherInputChange}
                      className="block w-full border border-gray-300 rounded p-2 mb-2"
                    />
                  )}
                </div>
              )}
              <p className="text-sm text-gray-500">{question.description}</p>
            </div>
          ))}
          <button
            type="submit"
            className="bg-violet-500 hover:bg-violet-700 text-white font-bold py-2 px-4 rounded focus:outline-none"
          >
            {formData.loading ? 'Submitting...' : 'Submit'}
          </button>
        </form>
        {children}
      </div>
    </div>
  );
};

export default FormPage;
