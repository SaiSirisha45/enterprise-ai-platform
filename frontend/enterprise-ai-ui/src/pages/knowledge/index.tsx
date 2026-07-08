import DashboardLayout from "../../layouts/DashboardLayout";
import DocumentUpload from "../../components/knowledge/DocumentUpload";
import DocumentSearch from "../../components/knowledge/DocumentSearch";
import DocumentList from "../../components/knowledge/DocumentList";
import ApprovalQueue from "../../components/knowledge/ApprovalQueue";

const Knowledge = () => {
  return (
    <DashboardLayout>
      <h1>Knowledge Base</h1>

      <DocumentUpload />

      <DocumentSearch />

      <DocumentList />

      <ApprovalQueue />
    </DashboardLayout>
  );
};

export default Knowledge; 