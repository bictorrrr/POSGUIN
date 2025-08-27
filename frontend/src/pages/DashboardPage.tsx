import { useState, useEffect } from "react";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import ContentArea from "../components/ContentArea";
import FooterBar from "../components/FooterBar";
import "./CSS/DashboardPage.css"

function DashboardPage() {
    const [sidebarExpanded, setSidebarExpanded] = useState(true);
    const [activeModule, setActiveModule] = useState("dashboard");
    const [activeSub, setActiveSub] = useState<string | null>(null);
    const [currentTime, setCurrentTime] = useState(new Date());
    const [notifications] = useState(3);

    useEffect(() => {
        const timer = setInterval(() => setCurrentTime(new Date()), 1000);
        return () => clearInterval(timer);
    }, []);

    return (
        <div className="Dash">
            <Sidebar
                expanded={sidebarExpanded}
                activeModule={activeModule}
                onToggle={() => setSidebarExpanded(!sidebarExpanded)}
                onSelect={(mod) => {
                    setActiveModule(mod);
                    setActiveSub(null);
                }}
            />
            <div className="Dashcontent">
                <Topbar activeModule={activeModule} activeSub={activeSub} onSubSelected={setActiveSub} />
                <ContentArea activeModule={activeModule} activeSub={activeSub} />
                <FooterBar currentTime={currentTime} notifications={notifications} />
            </div>
        </div>
    );
}


export default DashboardPage;
