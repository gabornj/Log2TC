function getFinalRe
    getTCPResult('./covInfo/space/stateFile.txt','./covInfo/space/stateGSO_AOTFD.txt');
    getTCPResult('./covInfo/space/newBlockFile.txt','./covInfo/space/blockGSO_AOTFD.txt');
    getTCPResult('./covInfo/space/branchFile.txt','./covInfo/space/branchGSO_AOTFD.txt');
%     getTCPResult('./covInfo/print_tokens/stateFile.txt','./covInfo/print_tokens/stateGSO_AOTFD.txt');
%     getTCPResult('./covInfo/print_tokens/newBlockFile.txt','./covInfo/print_tokens/blockGSO_AOTFD.txt');
%     getTCPResult('./covInfo/print_tokens/branchFile.txt','./covInfo/print_tokens/branchGSO_AOTFD.txt');
%     getTCPResult('./covInfo/print_tokens2/stateFile.txt','./covInfo/print_tokens2/stateGSO_AOTFD.txt');
%     getTCPResult('./covInfo/print_tokens2/newBlockFile.txt','./covInfo/print_tokens2/blockGSO_AOTFD.txt');
%     getTCPResult('./covInfo/print_tokens2/branchFile.txt','./covInfo/print_tokens2/branchGSO_AOTFD.txt');
%     getTCPResult('./covInfo/schedule/stateFile.txt','./covInfo/schedule/stateGSO_AOTFD.txt');
%     getTCPResult('./covInfo/schedule/newBlockFile.txt','./covInfo/schedule/blockGSO_AOTFD.txt');
%     getTCPResult('./covInfo/schedule/branchFile.txt','./covInfo/schedule/branchGSO_AOTFD.txt');
%     getTCPResult('./covInfo/schedule2/stateFile.txt','./covInfo/schedule2/stateGSO_AOTFD.txt');
%     getTCPResult('./covInfo/schedule2/newBlockFile.txt','./covInfo/schedule2/blockGSO_AOTFD.txt');
%     getTCPResult('./covInfo/schedule2/branchFile.txt','./covInfo/schedule2/branchGSO_AOTFD.txt');
%     getTCPResult('./covInfo/print_tokens/stateFile.txt','./covInfo/print_tokens/stateGAResult.txt');
%     getTCPResult('./covInfo/print_tokens/newBlockFile.txt','./covInfo/print_tokens/blockGAResult.txt');
%     getTCPResult('./covInfo/print_tokens/branchFile.txt','./covInfo/print_tokens/branchGAResult.txt');
%     getTCPResult('./covInfo/print_tokens2/stateFile.txt','./covInfo/print_tokens2/stateGAResult.txt');
%     getTCPResult('./covInfo/print_tokens2/newBlockFile.txt','./covInfo/print_tokens2/blockGAResult.txt');
%     getTCPResult('./covInfo/print_tokens2/branchFile.txt','./covInfo/print_tokens2/branchGAResult.txt');
%     getTCPResult('./covInfo/schedule/stateFile.txt','./covInfo/schedule/stateGAResult.txt');
%     getTCPResult('./covInfo/schedule/newBlockFile.txt','./covInfo/schedule/blockGAResult.txt');
%     getTCPResult('./covInfo/schedule/branchFile.txt','./covInfo/schedule/branchGAResult.txt');
%     getTCPResult('./covInfo/schedule2/stateFile.txt','./covInfo/schedule2/stateGAResult.txt');
%     getTCPResult('./covInfo/schedule2/newBlockFile.txt','./covInfo/schedule2/blockGAResult.txt');
%     getTCPResult('./covInfo/schedule2/branchFile.txt','./covInfo/schedule2/branchGAResult.txt');
%     getTCPResult('./covInfo/space/stateFile.txt','./covInfo/space/stateGAResult.txt');
%     getTCPResult('./covInfo/space/newBlockFile.txt','./covInfo/space/blockGAResult.txt');
%     getTCPResult('./covInfo/space/branchFile.txt','./covInfo/space/branchGAResult.txt');
%     getTCPResult('./covInfo/print_tokens/stateFile.txt','./covInfo/print_tokens/stateAGResult.txt');
%     getTCPResult('./covInfo/print_tokens/newBlockFile.txt','./covInfo/print_tokens/blockAGResult.txt');
%     getTCPResult('./covInfo/print_tokens/branchFile.txt','./covInfo/print_tokens/branchAGResult.txt');
%     getTCPResult('./covInfo/print_tokens2/stateFile.txt','./covInfo/print_tokens2/stateAGResult.txt');
%     getTCPResult('./covInfo/print_tokens2/newBlockFile.txt','./covInfo/print_tokens2/blockAGResult.txt');
%     getTCPResult('./covInfo/print_tokens2/branchFile.txt','./covInfo/print_tokens2/branchAGResult.txt');
%     getTCPResult('./covInfo/schedule/stateFile.txt','./covInfo/schedule/stateAGResult.txt');
%     getTCPResult('./covInfo/schedule/newBlockFile.txt','./covInfo/schedule/blockAGResult.txt');
%     getTCPResult('./covInfo/schedule/branchFile.txt','./covInfo/schedule/branchAGResult.txt');
%     getTCPResult('./covInfo/schedule2/stateFile.txt','./covInfo/schedule2/stateAGResult.txt');
%     getTCPResult('./covInfo/schedule2/newBlockFile.txt','./covInfo/schedule2/blockAGResult.txt');
%     getTCPResult('./covInfo/schedule2/branchFile.txt','./covInfo/schedule2/branchAGResult.txt');
%     getTCPResult('./covInfo/space/stateFile.txt','./covInfo/space/stateAGResult.txt');
%     getTCPResult('./covInfo/space/newBlockFile.txt','./covInfo/space/blockAGResult.txt');
%     getTCPResult('./covInfo/space/branchFile.txt','./covInfo/space/branchAGResult.txt');
%     getTCPResult('./covInfo/print_tokens/stateFile.txt','./covInfo/print_tokens/stateGSOResult.txt');
%     getTCPResult('./covInfo/print_tokens/newBlockFile.txt','./covInfo/print_tokens/blockGSOResult.txt');
%     getTCPResult('./covInfo/print_tokens/branchFile.txt','./covInfo/print_tokens/branchGSOResult.txt');
%     getTCPResult('./covInfo/print_tokens2/stateFile.txt','./covInfo/print_tokens2/stateGSOResult.txt');
%     getTCPResult('./covInfo/print_tokens2/newBlockFile.txt','./covInfo/print_tokens2/blockGSOResult.txt');
%     getTCPResult('./covInfo/print_tokens2/branchFile.txt','./covInfo/print_tokens2/branchGSOResult.txt');
%     getTCPResult('./covInfo/schedule/stateFile.txt','./covInfo/schedule/stateGSOResult.txt');
%     getTCPResult('./covInfo/schedule/newBlockFile.txt','./covInfo/schedule/blockGSOResult.txt');
%     getTCPResult('./covInfo/schedule/branchFile.txt','./covInfo/schedule/branchGSOResult.txt');
%     getTCPResult('./covInfo/schedule2/stateFile.txt','./covInfo/schedule2/stateGSOResult.txt');
%     getTCPResult('./covInfo/schedule2/newBlockFile.txt','./covInfo/schedule2/blockGSOResult.txt');
%     getTCPResult('./covInfo/schedule2/branchFile.txt','./covInfo/schedule2/branchGSOResult.txt');
%     getTCPResult('./covInfo/space/stateFile.txt','./covInfo/space/stateGSOResult.txt');
%     getTCPResult('./covInfo/space/newBlockFile.txt','./covInfo/space/blockGSOResult.txt');
%     getTCPResult('./covInfo/space/branchFile.txt','./covInfo/space/branchGSOResult.txt');
end