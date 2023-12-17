import OpenAI from 'openai';

const openai = new OpenAI({});

export default async function handler(req, res) {
  try {
    const { projectInfo } = req.body;

    // Prompt 1: Open Source Solutions Recommendations
    const prompt1Response = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a helpful assistant.' },
        { role: 'user', content: `From project details: ${projectInfo}`, role: 'assistant', content: 'Please suggest open source solutions that can be used to build the project.' },
      ],
      format: 'json',
    });

    const openSourceRecommendations = prompt1Response.choices[0]?.message?.content || 'No open source solutions recommended';

    // Prompt 2: Implementation Guidance
    const prompt2Response = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a helpful assistant.' },
        { role: 'user', content: `From project details: ${projectInfo}`, role: 'assistant', content: 'Now that we have identified potential open source solutions, please provide guidance on how to implement the recommended solutions in the project. Offer step-by-step instructions or a high-level overview of the implementation process.' },
      ],
      format: 'json',
    });

    const implementationGuidance = prompt2Response.choices[0]?.message?.content || 'No implementation guidance provided';

    // Prompt 3: Cost Minimization Strategies
    const prompt3Response = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a helpful assistant.' },
        { role: 'user', content: `From project details: ${projectInfo}`, role: 'assistant', content: 'Considering the project requirements, suggest strategies and approaches to minimize costs associated with the implementation. This can include optimizing resource usage, choosing cost-effective services, or any other recommendations that contribute to overall cost reduction. Present the information in a detailed and actionable manner.' },
      ],
      format: 'json',
    });

    const costMinimizationStrategies = prompt3Response.choices[0]?.message?.content || 'No cost minimization strategies suggested';

    res.status(200).json({
      openSourceRecommendations,
      implementationGuidance,
      costMinimizationStrategies,
    });
  } catch (error) {
    console.error('Error fetching recommendations:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
}
