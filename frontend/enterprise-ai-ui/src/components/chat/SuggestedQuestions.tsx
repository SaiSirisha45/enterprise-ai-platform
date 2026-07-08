const SuggestedQuestions = () => {
  const questions = [
    "What is RAG?",
    "Explain AI Agents",
    "Summarize this document",
  ];

  return (
    <div style={{ padding: "20px" }}>
      <h3>Suggested Questions</h3>

      {questions.map((question) => (
        <button
          key={question}
          style={{
            display: "block",
            marginBottom: "10px",
            padding: "10px",
          }}
        >
          {question}
        </button>
      ))}
    </div>
  );
};

export default SuggestedQuestions; 