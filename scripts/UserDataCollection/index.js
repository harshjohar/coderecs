import fetch from "node-fetch";
import fs from "fs";

const getData = async (contestId, start) => {
    const res = await fetch(
        `https://codeforces.com/api/contest.standings?contestId=${contestId}&from=${start}&count=10&showUnofficial=true`
    );
    const json = await res.json();

    if (res.status == 400) {
        const users = [];
        fs.appendFileSync("./output.json", JSON.stringify(users));

        if (contestId < 1600) {
            fs.appendFileSync("./output.json", ",");
        }
        return;
    }

    const users = json.result.rows.map((row) => {
        return row.party.members[0].handle;
    });

    fs.appendFileSync("./output.json", JSON.stringify(users));

    if (contestId < 1600) {
        fs.appendFileSync("./output.json", ",");
    }
};

async function run() {
    fs.appendFileSync("./output.json", "{");
    for (let index = 500; index <= 1600; index++) {
        fs.appendFileSync("./output.json", `\"${index}\":`);
        await getData(index, Math.floor(Math.random() * 10000));
    }
    fs.appendFileSync("./output.json", "}");
}

run();
