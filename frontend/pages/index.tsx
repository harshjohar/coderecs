import type { NextPage } from "next";
import Layout from "../components/common/Layout";

const problems = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}];
const problems2 = [{}, {}, {}, {}, {}];

const Home: NextPage = () => {
    return (
        <Layout>
            <div className="h-full w-full lg:flex rounded-xl space-y-3 lg:space-x-3 overflow-auto lg:overflow-hidden scrollbar-hide">
                
            </div>
        </Layout>
    );
};

export default Home;
