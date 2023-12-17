import { useState } from 'react';
import Link from 'next/link';
import axios from 'axios';
import projectData from '@/public/locales/en/project/identity.json';
import FormPage from '../../components/FormPage';

const Card = ({ title, content }) => (
  <div className="bg-white p-4 rounded shadow mb-4">
    <h3 className="text-xl font-semibold mb-2">{title}</h3>
    <p>{content}</p>
  </div>
);

const ProjectRecommendation = () => {
  const initialFormData = {
    ...projectData.reduce((acc, question) => ({ ...acc, [question.tag]: '' }), {}),
    loading: false,
  };

  const [formData, setFormData] = useState(initialFormData);
  const [recommendations, setRecommendations] = useState({});
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleCheckboxChange = (e) => {
    const { name, value, checked } = e.target;
    const currentValue = formData[name];

    setFormData({
      ...formData,
      [name]: checked ? [...currentValue, value] : currentValue.filter((val) => val !== value),
    });
  };

  const handleOtherInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const response = await axios.post('/api/recommendation', {
        projectInfo: JSON.stringify(formData),
      });
      setRecommendations(response.data);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <FormPage
        formData={formData}
        handleInputChange={handleInputChange}
        handleCheckboxChange={handleCheckboxChange}
        handleOtherInputChange={handleOtherInputChange}
        handleSubmit={handleSubmit}
        projectData={projectData}
      >
        {loading ? (
          <div className="mt-4 text-gray-600">Loading...</div>
        ) : (
          <div>
            {recommendations.openSourceRecommendations && (
              <Card title="Open Source Recommendations" content={recommendations.openSourceRecommendations} />
            )}
            {recommendations.implementationGuidance && (
              <Card title="Implementation Guidance" content={recommendations.implementationGuidance} />
            )}
            {recommendations.costMinimizationStrategies && (
              <Card title="Cost Minimization Strategies" content={recommendations.costMinimizationStrategies} />
            )}
            <Link href="/beta/apps" className="bg-blue-500 text-white px-4 py-2 rounded mt-4 inline-block">
                HyprSol Marketplace
            </Link>
          </div>

        )}
      </FormPage>
    </div>
  );
};

export default ProjectRecommendation;
