ace.define("ace/mode/assembly_x86_highlight_rules",["require","exports","module","ace/lib/oop","ace/mode/text_highlight_rules"],function(e,t,n){"use strict";var r=e("../lib/oop"),i=e("./text_highlight_rules").TextHighlightRules,s=function(){this.$rules={start:[{token:"keyword.control.assembly",regex:"\\b(?:__suuuuuuuuerlejrejroej_)\\b",caseInsensitive:!0},{token:"variable.parameter.register.assembly",regex:"\\b(?:const|sconst|comend|comstart|define|xse|jseval|setspeed|setmovespeed|label|lbl|funcstart|clearall|autosav|savfunc|clear|clearall|funcend|org|ret|return|end|compile|release|fcall|pageonbreak|setbreaklimit|breaklimit|autobreak|setautobreak)\\b",caseInsensitive:!0},{token:"constant.character.decimal.assembly",regex:"\\b[0-9]+\\b"},{token:"constant.character.hexadecimal.assembly",regex:"\\b0x[A-F0-9]+\\b",caseInsensitive:!0},{token:"constant.character.hexadecimal.assembly",regex:"\\b[A-F0-9]+h\\b",caseInsensitive:!0},{token:"support.function.directive.assembly",regex:"^\\[",push:[{defaultToken:"support.function.directive.assembly"}]},{token:["text","support.function.directive.assembly","text","entity.name.function.assembly"],regex:"(\\s*)(setflag|sf|addorg|move|rel|lock|goto|faceplayer|clearflag|resetflag|giveitem|item|cf|lf|l|lockface|lockfaceplayer|applymovement|warp|warpto|msg|msgbox|true|false|pokemon|givepokemon|applymovementnowait|movenowait)\\b( ?)((?:[][]*)?)",caseInsensitive:!0},{token:"support.function.directive.assembly",regex:"\\b(?:d[bwdqtoy]|res[bwdqto]|equ|times|align|alignb|sectalign|section|ptr|byte|word|dword|qword|incbin)\\b",caseInsensitive:!0},{token:"entity.name.function.assembly",regex:"^\\s*%%[\\w.]+?:$"},{token:"entity.name.function.assembly",regex:"^\\s*%\\$[\\w.]+?:$"},{token:"entity.name.function.assembly",regex:"^[\\w.]+?:"},{token:"entity.name.function.assembly",regex:"^[\\w.]+?\\b"},{token:"comment.assembly",regex:";.*$"}]},this.normalizeRules()};s.metaData={fileTypes:["asm"],name:"Assembly x86",scopeName:"source.assembly"},r.inherits(s,i),t.AssemblyX86HighlightRules=s}),ace.define("ace/mode/folding/coffee",["require","exports","module","ace/lib/oop","ace/mode/folding/fold_mode","ace/range"],function(e,t,n){"use strict";var r=e("../../lib/oop"),i=e("./fold_mode").FoldMode,s=e("../../range").Range,o=t.FoldMode=function(){};r.inherits(o,i),function(){this.getFoldWidgetRange=function(e,t,n){var r=this.indentationBlock(e,n);if(r)return r;var i=/\S/,o=e.getLine(n),u=o.search(i);if(u==-1||o[u]!="#")return;var a=o.length,f=e.getLength(),l=n,c=n;while(++n<f){o=e.getLine(n);var h=o.search(i);if(h==-1)continue;if(o[h]!="#")break;c=n}if(c>l){var p=e.getLine(c).length;return new s(l,a,c,p)}},this.getFoldWidget=function(e,t,n){var r=e.getLine(n),i=r.search(/\S/),s=e.getLine(n+1),o=e.getLine(n-1),u=o.search(/\S/),a=s.search(/\S/);if(i==-1)return e.foldWidgets[n-1]=u!=-1&&u<a?"start":"","";if(u==-1){if(i==a&&r[i]=="#"&&s[i]=="#")return e.foldWidgets[n-1]="",e.foldWidgets[n+1]="","start"}else if(u==i&&r[i]=="#"&&o[i]=="#"&&e.getLine(n-2).search(/\S/)==-1)return e.foldWidgets[n-1]="start",e.foldWidgets[n+1]="","";return u!=-1&&u<i?e.foldWidgets[n-1]="start":e.foldWidgets[n-1]="",i<a?"start":""}}.call(o.prototype)}),ace.define("ace/mode/assembly_x86",["require","exports","module","ace/lib/oop","ace/mode/text","ace/mode/assembly_x86_highlight_rules","ace/mode/folding/coffee"],function(e,t,n){"use strict";var r=e("../lib/oop"),i=e("./text").Mode,s=e("./assembly_x86_highlight_rules").AssemblyX86HighlightRules,o=e("./folding/coffee").FoldMode,u=function(){this.HighlightRules=s,this.foldingRules=new o,this.$behaviour=this.$defaultBehaviour};r.inherits(u,i),function(){this.lineCommentStart=[";"],this.$id="ace/mode/assembly_x86"}.call(u.prototype),t.Mode=u});                (function() {
                    ace.require(["ace/mode/assembly_x86"], function(m) {
                        if (typeof module == "object" && typeof exports == "object" && module) {
                            module.exports = m;
                        }
                    });
                })();
            