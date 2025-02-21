/** @odoo-module **/

/* Copyright 2025 ACSONE SA/NV
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html) */

import {rpc} from "@web/core/network/rpc";
import {session} from "@web/session";

let SESSION_TIMEOUT = 15000;

rpc("/web/session/get_timeout", {}).then((timeout) => {
    SESSION_TIMEOUT = parseInt(timeout, 10) || SESSION_TIMEOUT;
});

function getLastActivityTime() {
    return (
        parseInt(globalThis.window.localStorage.getItem("lastActivityTime"), 10) ||
        Date.now()
    );
}

function updateActivityTime() {
    const now = Date.now();
    globalThis.window.localStorage.setItem("lastActivityTime", now);
}

function closeSession() {
    rpc("/web/session/destroy", {}).then(() => {
        globalThis.window.location.reload();
    });
}

function checkInactivity() {
    const now = Date.now();
    const lastActivityTime = getLastActivityTime();
    if (now - lastActivityTime >= SESSION_TIMEOUT) {
        closeSession();
    }
}

function startSessionAutoClose() {
    if (!session) {
        return;
    }

    function handleUserActivity() {
        updateActivityTime();
    }

    globalThis.window.addEventListener("mousemove", handleUserActivity);
    globalThis.window.addEventListener("keydown", handleUserActivity);
    updateActivityTime();
    globalThis.setInterval(checkInactivity, SESSION_TIMEOUT / 2);
}

startSessionAutoClose();
