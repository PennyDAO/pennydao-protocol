// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import {
    ERC1155PresetMinterPauser
} from "openzeppelin/contracts/token/ERC1155/presets/ERC1155PresetMinterPauser.sol";
import {Counters} from "openzeppelin/contracts/utils/Counters.sol";

/// @title Entrypoint to the PennyDAO protocol
/// @author PennyDAO
contract PennyDAO is ERC1155PresetMinterPauser {
    using Counters for Counters.Counter;

    event ApplicationCreated(
        address indexed applicant,
        uint256 indexed applicationId,
        string ipfsCID
    );

    Counters.Counter private _tokenIdTracker;

    constructor(string memory uri) ERC1155PresetMinterPauser(uri) {
        // the first tokenId will be the pennyToken
        _tokenIdTracker.increment();
    }

    /// @notice Allow student to apply for a grant
    /// @dev Takes an IPFS CID as an argument for data location
    /// @param _ipfsCID a valid ipfs CID
    /// @return The NFT id minted representing an application
    function createApplication(string memory _ipfsCID)
        external
        returns (uint256)
    {
        uint256 id = _tokenIdTracker.current();
        _mint(_msgSender(), id, 1, "");
        _tokenIdTracker.increment();
        emit ApplicationCreated(_msgSender(), id, _ipfsCID);
        return id;
    }
}
