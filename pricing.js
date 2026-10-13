// Pricing config for the marketing page.
// Tier names are the only place to rename the packages. They are not final.
// Card titles, the Get CTAs, and "Everything in {desk}." all read TIER_NAMES.
var TIER_NAMES = {
  desk: "Desk",
  floor: "Floor"
};

// placeholderPrices: every price reads "Price coming soon" and the Yearly
// toggle reads "Yearly billing available". Flip it off only when real
// monthly and yearlyPerMonth amounts are set. yearlyPerMonth is the monthly
// rate when billed yearly, not the annual total.
// paidCheckout: off. CTAs use the access request. There is no payment URL.
var PRICING = {
  placeholderPrices: true,
  paidCheckout: false,
  tiers: {
    desk: { connections: 1, monthly: null, yearlyPerMonth: null },
    floor: { connections: 10, monthly: null, yearlyPerMonth: null }
  },
  venues: [
    { id: "hyperliquid", coming: false },
    { id: "bybit", coming: true },
    { id: "mt5", coming: true }
  ]
};

var PRICE_COMING_SOON = "Price coming soon";
var YEARLY_BILLING_AVAILABLE = "Yearly billing available";

function yearlySavingsPercent(monthly, yearlyPerMonth) {
  if (typeof monthly !== "number" || typeof yearlyPerMonth !== "number") return null;
  if (!isFinite(monthly) || !isFinite(yearlyPerMonth)) return null;
  if (monthly <= 0 || yearlyPerMonth < 0) return null;
  return Math.round(((monthly - yearlyPerMonth) / monthly) * 100);
}

function formatDollars(amount) {
  if (typeof amount !== "number" || !isFinite(amount) || amount < 0) return null;
  var cents = Math.round(amount * 100);
  var whole = Math.floor(cents / 100);
  var rem = cents % 100;
  var body = String(whole).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  if (rem !== 0) {
    body += "." + (rem < 10 ? "0" : "") + rem;
  }
  return "$" + body;
}

function priceLabel(placeholderPrices, monthly, yearlyPerMonth, period) {
  if (placeholderPrices) return PRICE_COMING_SOON;
  var amount = period === "yearly" ? yearlyPerMonth : monthly;
  var formatted = formatDollars(amount);
  if (formatted === null) return PRICE_COMING_SOON;
  if (period === "yearly") return formatted + " per month, billed yearly";
  return formatted + " per month";
}

function saveLine(percent) {
  if (typeof percent !== "number" || percent < 0) return null;
  return "Save " + percent + "% with yearly";
}

// One line for the Yearly toggle when every tier yields the same percent.
// Returns null when live percents differ, so each card states its own.
function yearlyToggleLabel(placeholderPrices, tiers) {
  if (placeholderPrices) return YEARLY_BILLING_AVAILABLE;
  var keys = Object.keys(tiers);
  if (!keys.length) return YEARLY_BILLING_AVAILABLE;
  var percents = [];
  for (var i = 0; i < keys.length; i++) {
    var tier = tiers[keys[i]];
    var pct = yearlySavingsPercent(tier.monthly, tier.yearlyPerMonth);
    if (pct === null) return YEARLY_BILLING_AVAILABLE;
    percents.push(pct);
  }
  var first = percents[0];
  for (var j = 1; j < percents.length; j++) {
    if (percents[j] !== first) return null;
  }
  return saveLine(first) || YEARLY_BILLING_AVAILABLE;
}

function connectionLabel(count) {
  if (count === 1) return "1 connection";
  return "Up to " + count + " connections";
}

function tierCta(name) {
  return "Get " + name;
}

function everythingInLine(deskName) {
  return "Everything in " + deskName + ".";
}

function applyTierNames(doc) {
  Object.keys(TIER_NAMES).forEach(function (key) {
    var name = TIER_NAMES[key];
    doc.querySelectorAll('[data-tier-name="' + key + '"]').forEach(function (el) {
      el.textContent = name;
    });
    doc.querySelectorAll('[data-tier-cta="' + key + '"]').forEach(function (el) {
      el.textContent = tierCta(name);
      if (!PRICING.paidCheckout && el.tagName === "A") el.removeAttribute("href");
    });
  });
  doc.querySelectorAll("[data-everything-in]").forEach(function (el) {
    el.textContent = everythingInLine(TIER_NAMES.desk);
  });
  Object.keys(PRICING.tiers).forEach(function (key) {
    var count = PRICING.tiers[key].connections;
    doc.querySelectorAll('.plan[data-tier="' + key + '"]').forEach(function (el) {
      el.setAttribute("data-connections", String(count));
    });
    doc.querySelectorAll('[data-tier-limit="' + key + '"]').forEach(function (el) {
      el.textContent = connectionLabel(count);
    });
  });
}

function renderPrices(doc, period) {
  var section = doc.getElementById("pricing");
  if (section) section.setAttribute("data-billing", period);
  Object.keys(PRICING.tiers).forEach(function (key) {
    var tier = PRICING.tiers[key];
    doc.querySelectorAll('[data-price="' + key + '"]').forEach(function (el) {
      el.textContent = priceLabel(PRICING.placeholderPrices, tier.monthly, tier.yearlyPerMonth, period);
    });
  });

  var shared = yearlyToggleLabel(PRICING.placeholderPrices, PRICING.tiers);
  var note = doc.getElementById("yearly-note");
  if (note) {
    if (shared) {
      note.hidden = false;
      note.textContent = shared;
    } else {
      note.hidden = true;
      note.textContent = "";
    }
  }

  Object.keys(PRICING.tiers).forEach(function (key) {
    doc.querySelectorAll('[data-save="' + key + '"]').forEach(function (el) {
      if (PRICING.placeholderPrices || shared) {
        el.hidden = true;
        el.textContent = "";
        return;
      }
      var tier = PRICING.tiers[key];
      var line = saveLine(yearlySavingsPercent(tier.monthly, tier.yearlyPerMonth));
      el.hidden = !line;
      el.textContent = line || "";
    });
  });
}

function venueById(id) {
  for (var i = 0; i < PRICING.venues.length; i++) {
    if (PRICING.venues[i].id === id) return PRICING.venues[i];
  }
  return null;
}

function bindVenues(doc) {
  var buttons = doc.querySelectorAll("#pricing [data-venue]");
  buttons.forEach(function (btn) {
    var spec = venueById(btn.getAttribute("data-venue"));
    var coming = spec ? spec.coming === true : btn.getAttribute("data-coming") === "true";
    if (coming) {
      btn.disabled = true;
      btn.setAttribute("data-coming", "true");
      btn.setAttribute("aria-disabled", "true");
      btn.setAttribute("aria-pressed", "false");
    }
    btn.addEventListener("click", function (event) {
      if (coming || btn.disabled || btn.getAttribute("data-coming") === "true") {
        event.preventDefault();
        event.stopPropagation();
        btn.disabled = true;
        btn.setAttribute("aria-pressed", "false");
        return;
      }
      buttons.forEach(function (other) {
        if (other.disabled || other.getAttribute("data-coming") === "true") {
          other.setAttribute("aria-pressed", "false");
          return;
        }
        other.setAttribute("aria-pressed", other === btn ? "true" : "false");
      });
    });
  });
}

function bindToggle(doc) {
  var buttons = doc.querySelectorAll("#pricing [data-period]");
  var order = ["monthly", "yearly"];

  function select(period) {
    buttons.forEach(function (btn) {
      var on = btn.getAttribute("data-period") === period;
      btn.setAttribute("aria-checked", on ? "true" : "false");
      btn.tabIndex = on ? 0 : -1;
    });
    var section = doc.getElementById("pricing");
    if (section) section.setAttribute("data-billing", period);
    renderPrices(doc, period);
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      select(btn.getAttribute("data-period"));
    });
  });

  var group = doc.querySelector("#pricing .bill-toggle");
  if (!group) return;
  group.addEventListener("keydown", function (event) {
    if (event.key !== "ArrowRight" && event.key !== "ArrowLeft") return;
    event.preventDefault();
    var current = doc.querySelector('#pricing [data-period][aria-checked="true"]');
    var idx = order.indexOf(current ? current.getAttribute("data-period") : "monthly");
    if (idx < 0) idx = 0;
    if (event.key === "ArrowRight") idx = Math.min(order.length - 1, idx + 1);
    if (event.key === "ArrowLeft") idx = Math.max(0, idx - 1);
    select(order[idx]);
    buttons[idx].focus();
  });
}

function mount(doc) {
  if (!doc || !doc.getElementById || !doc.getElementById("pricing")) return;
  applyTierNames(doc);
  bindToggle(doc);
  bindVenues(doc);
  renderPrices(doc, "monthly");
}

var HANDLD_PRICING = {
  TIER_NAMES: TIER_NAMES,
  PRICING: PRICING,
  PRICE_COMING_SOON: PRICE_COMING_SOON,
  YEARLY_BILLING_AVAILABLE: YEARLY_BILLING_AVAILABLE,
  yearlySavingsPercent: yearlySavingsPercent,
  formatDollars: formatDollars,
  priceLabel: priceLabel,
  yearlyToggleLabel: yearlyToggleLabel,
  connectionLabel: connectionLabel,
  tierCta: tierCta,
  everythingInLine: everythingInLine,
  mount: mount
};

if (typeof module === "object" && module.exports) {
  module.exports = HANDLD_PRICING;
}
if (typeof window !== "undefined") {
  window.HANDLD_PRICING = HANDLD_PRICING;
}
