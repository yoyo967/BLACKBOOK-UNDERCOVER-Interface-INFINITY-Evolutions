/* @ds-bundle: {"format":4,"namespace":"AgenticumDesignSystem_afffd0","components":[{"name":"ChapterKicker","sourcePath":"components/book/ChapterKicker.jsx"},{"name":"QRPanel","sourcePath":"components/book/QRPanel.jsx"},{"name":"RadarMotif","sourcePath":"components/book/RadarMotif.jsx"},{"name":"Badge","sourcePath":"components/core/Badge.jsx"},{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"Divider","sourcePath":"components/core/Divider.jsx"},{"name":"DualLayerBlock","sourcePath":"components/core/DualLayerBlock.jsx"},{"name":"GlassCard","sourcePath":"components/core/GlassCard.jsx"}],"sourceHashes":{"components/book/ChapterKicker.jsx":"5eecdf3f7c4a","components/book/QRPanel.jsx":"796491006d22","components/book/RadarMotif.jsx":"57d0e024f8a1","components/core/Badge.jsx":"c68c40cc13db","components/core/Button.jsx":"c79d6bdfd32f","components/core/Divider.jsx":"4a6880c3a9e6","components/core/DualLayerBlock.jsx":"3a2a81e5c087","components/core/GlassCard.jsx":"863869a03137"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.AgenticumDesignSystem_afffd0 = window.AgenticumDesignSystem_afffd0 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/book/ChapterKicker.jsx
try { (() => {
function ChapterKicker({
  series,
  band
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: '4px',
      alignItems: 'center',
      textAlign: 'center'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-mono)',
      fontSize: '13px',
      letterSpacing: '0.2em',
      textTransform: 'uppercase',
      color: 'var(--fg-mute)'
    }
  }, series), band && /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-mono)',
      fontSize: '12px',
      letterSpacing: '0.16em',
      textTransform: 'uppercase',
      color: 'var(--signal-bright)'
    }
  }, band));
}
Object.assign(__ds_scope, { ChapterKicker });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/book/ChapterKicker.jsx", error: String((e && e.message) || e) }); }

// components/book/QRPanel.jsx
try { (() => {
function QRPanel({
  url,
  size = 96
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: '16px'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      width: size,
      height: size,
      background: 'var(--fg)',
      borderRadius: '8px',
      display: 'grid',
      placeItems: 'center',
      flexShrink: 0
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-mono)',
      fontSize: '10px',
      color: 'var(--bg)',
      textAlign: 'center',
      padding: '4px'
    }
  }, "QR")), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-mono)',
      fontSize: '12px',
      color: 'var(--fg-mute)',
      wordBreak: 'break-all'
    }
  }, url));
}
Object.assign(__ds_scope, { QRPanel });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/book/QRPanel.jsx", error: String((e && e.message) || e) }); }

// components/book/RadarMotif.jsx
try { (() => {
function RadarMotif({
  size = 200,
  pulse = true
}) {
  const rings = [1, 0.75, 0.5, 0.28];
  return /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'relative',
      width: size,
      height: size
    }
  }, rings.map((r, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    style: {
      position: 'absolute',
      inset: 0,
      margin: 'auto',
      width: size * r,
      height: size * r,
      borderRadius: '50%',
      border: '1px solid rgba(6,182,212,' + (0.15 + i * 0.12) + ')'
    }
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'absolute',
      inset: 0,
      margin: 'auto',
      width: '6px',
      height: '6px',
      borderRadius: '50%',
      background: 'var(--signal-bright)',
      boxShadow: '0 0 24px 6px rgba(34,211,238,.6)',
      animation: pulse ? 'radarPulse 2.4s ease-in-out infinite' : 'none'
    }
  }), /*#__PURE__*/React.createElement("style", null, '@keyframes radarPulse{0%,100%{opacity:.6;transform:scale(1)}50%{opacity:1;transform:scale(1.3)}}'));
}
Object.assign(__ds_scope, { RadarMotif });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/book/RadarMotif.jsx", error: String((e && e.message) || e) }); }

// components/core/Badge.jsx
try { (() => {
function Badge({
  children,
  tone = 'neutral',
  mono = false
}) {
  const tones = {
    neutral: {
      background: 'var(--bg-surface)',
      color: 'var(--fg-mute)',
      border: '1px solid var(--line)'
    },
    signal: {
      background: 'rgba(6,182,212,.12)',
      color: 'var(--signal-bright)',
      border: '1px solid rgba(6,182,212,.35)'
    },
    outline: {
      background: 'transparent',
      color: 'var(--fg-dim)',
      border: '1px solid var(--line)'
    }
  };
  return /*#__PURE__*/React.createElement("span", {
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: '6px',
      padding: '4px 12px',
      borderRadius: 'var(--radius-full)',
      fontSize: '12px',
      fontFamily: mono ? 'var(--font-mono)' : 'var(--font-body)',
      letterSpacing: mono ? '0.06em' : '0.02em',
      textTransform: mono ? 'uppercase' : 'none',
      ...tones[tone]
    }
  }, children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Badge.jsx", error: String((e && e.message) || e) }); }

// components/core/Button.jsx
try { (() => {
function Button({
  variant = 'primary',
  size = 'md',
  children,
  disabled,
  onClick,
  style
}) {
  const sizes = {
    sm: {
      padding: '8px 16px',
      fontSize: '13px'
    },
    md: {
      padding: '12px 24px',
      fontSize: '15px'
    },
    lg: {
      padding: '16px 32px',
      fontSize: '16px'
    }
  };
  const base = {
    fontFamily: 'var(--font-body)',
    fontWeight: 600,
    letterSpacing: '0.01em',
    borderRadius: 'var(--radius-full)',
    border: '1px solid transparent',
    cursor: disabled ? 'not-allowed' : 'pointer',
    opacity: disabled ? 0.45 : 1,
    transition: 'all var(--duration-standard) var(--ease-standard)',
    display: 'inline-flex',
    alignItems: 'center',
    gap: '8px',
    ...sizes[size]
  };
  const variants = {
    primary: {
      background: 'var(--signal)',
      color: '#01131a',
      boxShadow: '0 0 24px rgba(6,182,212,.35)'
    },
    secondary: {
      background: 'transparent',
      color: 'var(--fg)',
      border: '1px solid var(--line)'
    },
    ghost: {
      background: 'transparent',
      color: 'var(--signal-bright)',
      border: '1px solid transparent'
    }
  };
  return /*#__PURE__*/React.createElement("button", {
    disabled: disabled,
    onClick: onClick,
    style: {
      ...base,
      ...variants[variant],
      ...style
    },
    onMouseEnter: e => {
      if (disabled) return;
      if (variant === 'primary') e.currentTarget.style.background = 'var(--signal-bright)';
      if (variant === 'secondary') e.currentTarget.style.borderColor = 'var(--signal)';
      if (variant === 'ghost') e.currentTarget.style.color = 'var(--fg)';
    },
    onMouseLeave: e => {
      if (disabled) return;
      if (variant === 'primary') e.currentTarget.style.background = 'var(--signal)';
      if (variant === 'secondary') e.currentTarget.style.borderColor = 'var(--line)';
      if (variant === 'ghost') e.currentTarget.style.color = 'var(--signal-bright)';
    }
  }, children);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/Divider.jsx
try { (() => {
function Divider({
  label,
  style
}) {
  if (!label) return /*#__PURE__*/React.createElement("hr", {
    style: {
      border: 'none',
      borderTop: '1px solid var(--line)',
      margin: '24px 0',
      ...style
    }
  });
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: '12px',
      margin: '24px 0',
      ...style
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      height: '1px',
      background: 'linear-gradient(90deg,transparent,var(--line))'
    }
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-mono)',
      fontSize: '11px',
      letterSpacing: '0.16em',
      textTransform: 'uppercase',
      color: 'var(--signal-bright)'
    }
  }, label), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      height: '1px',
      background: 'linear-gradient(270deg,transparent,var(--line))'
    }
  }));
}
Object.assign(__ds_scope, { Divider });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Divider.jsx", error: String((e && e.message) || e) }); }

// components/core/DualLayerBlock.jsx
try { (() => {
function DualLayerBlock({
  labelA = 'Schicht A',
  titleA,
  textA,
  labelB = 'Schicht B',
  titleB,
  textB
}) {
  const wrap = {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '1px',
    background: 'var(--line)',
    border: '1px solid var(--line)',
    borderRadius: 'var(--radius)',
    overflow: 'hidden'
  };
  const pane = (bg, fg) => ({
    background: bg,
    padding: '24px',
    display: 'flex',
    flexDirection: 'column',
    gap: '8px'
  });
  return /*#__PURE__*/React.createElement("div", {
    style: wrap
  }, /*#__PURE__*/React.createElement("div", {
    style: pane('var(--fg)')
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-mono)',
      fontSize: '11px',
      letterSpacing: '0.16em',
      textTransform: 'uppercase',
      color: 'var(--signal-deep)'
    }
  }, labelA), /*#__PURE__*/React.createElement("strong", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: '18px',
      color: '#020617'
    }
  }, titleA), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: '14px',
      color: '#334155',
      lineHeight: 1.6,
      margin: 0
    }
  }, textA)), /*#__PURE__*/React.createElement("div", {
    style: pane('var(--bg-elevated)')
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-mono)',
      fontSize: '11px',
      letterSpacing: '0.16em',
      textTransform: 'uppercase',
      color: 'var(--signal-bright)'
    }
  }, labelB), /*#__PURE__*/React.createElement("strong", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: '18px',
      color: 'var(--fg)'
    }
  }, titleB), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: '14px',
      color: 'var(--fg-mute)',
      lineHeight: 1.6,
      margin: 0
    }
  }, textB)));
}
Object.assign(__ds_scope, { DualLayerBlock });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/DualLayerBlock.jsx", error: String((e && e.message) || e) }); }

// components/core/GlassCard.jsx
try { (() => {
function GlassCard({
  children,
  strong = false,
  glow = false,
  style
}) {
  const cls = strong ? 'glass-strong' : 'glass';
  return /*#__PURE__*/React.createElement("div", {
    className: cls,
    style: {
      padding: '24px',
      boxShadow: glow ? 'inset 0 1px 1px var(--glass-highlight), var(--glass-shadow), var(--glass-glow)' : undefined,
      ...style
    }
  }, children);
}
Object.assign(__ds_scope, { GlassCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/GlassCard.jsx", error: String((e && e.message) || e) }); }

__ds_ns.ChapterKicker = __ds_scope.ChapterKicker;

__ds_ns.QRPanel = __ds_scope.QRPanel;

__ds_ns.RadarMotif = __ds_scope.RadarMotif;

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Divider = __ds_scope.Divider;

__ds_ns.DualLayerBlock = __ds_scope.DualLayerBlock;

__ds_ns.GlassCard = __ds_scope.GlassCard;

})();
